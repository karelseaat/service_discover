# service_discover

UDP-based service discovery. I built this because I needed a simple way for services to find each other on a local network—no external dependencies, no over-engineering.

## Requirements

- Python 3.9+  
- Dependencies (`twisted`, `pyyaml`) via `Pipfile`:
  ```bash
  pipenv install
  ```

## Files

| File | Purpose |
|------|---------|
| `client.py` | Queries the server and prints available services |
| `server.py` | Answers client queries using definitions from `settings.yml` |
| `message.py` | Encodes/decodes UDP packets (fixed 128-byte max) |
| `settings.yml` | Server’s static service registry |
| `Pipfile` | Pipenv dependency spec |

## Usage

### Start the server

```bash
pipenv run python server.py
```

The server listens on UDP port `9000` by default and reads `settings.yml` on every request. Changes to `settings.yml` take effect immediately.

### Run the client

```bash
pipenv run python client.py
```

The client broadcasts a UDP packet, waits up to 2 seconds for a response, then prints services in YAML format.

## Configuration

Edit `settings.yml` to add/remove services:

```yaml
servers:
  - socialgames:
      proto: TCP
      ip: 0.0.0.0
      port: 4242
```

The server only serves services defined here. No dynamic registration—this is for static environments.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT — see [`LICENSE`](LICENSE).