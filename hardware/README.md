# GarAdhocApp hardware assignment

These CSV files belong to the sensor demo application. They describe the
components, Linux device paths, simulated drivers, and Raspberry Pi wiring
consumed by GAR at runtime.

Target Packs in `gar-tools/targets/` describe reusable board/runtime
capabilities only. GAR resolves this directory from the product workspace and
passes it to the selected target runtime as `GAR_HARDWARE_DIR`.


Board/OS resources are selected from `sources/board-raspberry-pi-5` by product.json.
The Product CSVs keep the sensor choices and their uses. Offline composition
validation covers GPIO, SPI and I2C; physical deployment remains planned.
See [composition](../docs/COMPOSITION.md).
