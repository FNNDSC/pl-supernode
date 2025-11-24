# FedMed Flower SuperNode

This plugin packages a Flower SuperNode inside a ChRIS-friendly container. Run the commands below from inside `plugins/supernode_plugin/`. The actual training loop only knows how to fit a local logistic regression model; Flower merely orchestrates the parameter exchange.

## Build
```bash
docker build -t fedmed/pl-supernode .
```

## Run (example)
```bash
docker run --rm --name fedmed-supernode --network fedmed-net \
  -v $(pwd)/demo/client-in:/incoming:ro \
  -v $(pwd)/demo/client-out:/outgoing:rw \
  fedmed/pl-supernode \
    fedmed-pl-supernode --cid 0 --total-clients 1 \
    --superlink-host ${FEDMED_SUPERLINK_IP} --superlink-port 9092 \
    /incoming /outgoing
```

Make sure `${FEDMED_SUPERLINK_IP}` is populated via `docker inspect fedmed-superlink` (see the SuperLink README). After the Flower round completes, the plugin writes `client_metrics.json` into `/outgoing` so downstream ChRIS components (or you) can inspect the results.
