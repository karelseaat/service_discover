# service_discover

A lightweight UDP-based service discovery system in Python. Clients query a central server to learn about available services on the network.

## Requirements

- Python 3.9+  
- Dependencies (`twisted`, `pyyaml`) are managed via `Pipfile` — install with:
  ```bash
  pipenv install
  ```

## Files

| File | Purpose |
|------|---------|
| `client.py` | Client script — connects to the discovery server and prints available services |
| `server.py` | Server script — listens for client requests and broadcasts service info |
| `message.py` | Shared utility for encoding/decoding discovery messages |
| `settings.yml` | Configures services offered by the server |
| `Pipfile` | Pipenv dependency specification |

## Usage

### Start the server

```bash
pipenv run python server.py
```

The server listens for incoming client requests and serves service definitions from `settings.yml`.

### Run the client

```bash
pipenv run python client.py
```

The client connects to the server and prints the list of known services in real time.

## Configuration

Edit `settings.yml` to define services:

```yaml
servers:
  - socialgames:
      proto: TCP
      ip: 0.0.0.0
      port: 4242
```

Add or remove entries as needed. The server reads this file each time it responds to a client.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

## License

MIT — see [`LICENSE`](LICENSE) for terms.