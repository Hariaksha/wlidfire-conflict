"""
Generate maps of conflict events and wildfire detections across Indonesia for the
2015-02 to 2025-06 sample period used in the paper. Reads the same raw ACLED and VIIRS
fire data used in wind-IV.ipynb, and writes two figures to ../paper/figures/.
"""
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path

# ── Paths (same raw inputs as wind-IV.ipynb) ────────────────────────────────
ACLED_XLSX   = '/Users/hariaksha/Documents/GitHub/climate-conflict/data/unrest/ACLED Data_2026-06-10.xlsx'
FIRE_CSV     = '/Users/hariaksha/Documents/GitHub/climate-conflict/data/climate/fire/DL_FIRE_SUOMI-VIIRS-C2_718931_Nov2000-Feb2026_buffer0km-csv/fire_archive_SV-C2_718931.csv'
DISTRICT_SHP = '/Users/hariaksha/Documents/GitHub/climate-conflict/data/administrative/gadm41_IDN_shp/gadm41_IDN_2.shp'
OUT_DIR      = Path('/Users/hariaksha/Documents/GitHub/climate-conflict/paper/figures')
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Sample window (matches the paper's panel: Feb 2015 - Jun 2025) ──────────
START_DATE = pd.Timestamp('2015-02-01')
END_DATE   = pd.Timestamp('2025-06-30')

print('Loading administrative boundaries for the basemap...')
districts_gdf = gpd.read_file(DISTRICT_SHP)[['geometry']]
indonesia_outline = districts_gdf.dissolve()
print(f'  {len(districts_gdf):,} district polygons loaded.')

# ============================================================================
# Conflict events map (ACLED)
# ============================================================================
print('\nLoading ACLED conflict data...')
acled = pd.read_excel(
    ACLED_XLSX,
    usecols=['event_date', 'event_type', 'latitude', 'longitude']
)
acled['event_date'] = pd.to_datetime(acled['event_date'])
acled = acled[(acled['event_date'] >= START_DATE) & (acled['event_date'] <= END_DATE)].copy()
print(f'  {len(acled):,} conflict events in sample window '
      f'({START_DATE.date()} to {END_DATE.date()})')

conflict_gdf = gpd.GeoDataFrame(
    acled,
    geometry=gpd.points_from_xy(acled['longitude'], acled['latitude']),
    crs='EPSG:4326'
)

fig, ax = plt.subplots(figsize=(10, 8))
indonesia_outline.boundary.plot(ax=ax, color='black', linewidth=0.4)
conflict_gdf.plot(
    ax=ax, markersize=2, alpha=0.25, color='crimson', linewidth=0
)
ax.set_title(f'ACLED Conflict Events in Indonesia\n'
             f'{START_DATE.strftime("%b %Y")} – {END_DATE.strftime("%b %Y")} '
             f'(n = {len(acled):,})', fontsize=13)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_aspect('equal')
fig.tight_layout()
conflict_out = OUT_DIR / 'conflict_events_map.png'
fig.savefig(conflict_out, dpi=300)
plt.close(fig)
print(f'  Saved: {conflict_out}')

# ============================================================================
# Wildfire detections map (VIIRS)
# ============================================================================
print('\nLoading VIIRS fire detections...')
fires_raw = pd.read_csv(
    FIRE_CSV,
    usecols=['acq_date', 'latitude', 'longitude', 'frp', 'confidence', 'type'],
    dtype={'confidence': str, 'type': int}
)
fires = fires_raw[
    (fires_raw['type'] == 0) &
    (fires_raw['confidence'].isin(['h', 'n']))
].copy()
fires['acq_date'] = pd.to_datetime(fires['acq_date'])
fires = fires[(fires['acq_date'] >= START_DATE) & (fires['acq_date'] <= END_DATE)].copy()
print(f'  {len(fires):,} vegetation-fire detections (type=0, confidence h/n) in sample window')

fire_gdf = gpd.GeoDataFrame(
    fires,
    geometry=gpd.points_from_xy(fires['longitude'], fires['latitude']),
    crs='EPSG:4326'
)

fig, ax = plt.subplots(figsize=(10, 8))
indonesia_outline.boundary.plot(ax=ax, color='black', linewidth=0.4)
sc = ax.scatter(
    fires['longitude'], fires['latitude'],
    s=2, c=np.log1p(fires['frp']), cmap='YlOrRd', alpha=0.3, linewidths=0
)
cbar = fig.colorbar(sc, ax=ax, fraction=0.03, pad=0.02)
cbar.set_label('log(1 + Fire Radiative Power)')
ax.set_title(f'VIIRS Wildfire Detections in Indonesia\n'
             f'{START_DATE.strftime("%b %Y")} – {END_DATE.strftime("%b %Y")} '
             f'(n = {len(fires):,})', fontsize=13)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_aspect('equal')
fig.tight_layout()
fire_out = OUT_DIR / 'wildfire_events_map.png'
fig.savefig(fire_out, dpi=300)
plt.close(fig)
print(f'  Saved: {fire_out}')

print('\nDone. Figures written to:', OUT_DIR)
