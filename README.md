 # service_discover GitHub Repository

Welcome to `service_discover`, a simple UDP-based client-server discovery system in Python. This project is designed for developers seeking an easy way to discover available services on a network.

## Requirements

To get started with this project, you'll need the following:

1. Python 3.9 (as specified in `Pipfile`)
2. The `twisted` and `pyyaml` libraries (automatically installed through `Pipfile`)

## Project Structure

The repository includes the following files and directories:

- `Pipfile`: A Pipenv file defining dependencies for this project.
- `client.py`: The entry point for the client application, which connects to a discovery server and retrieves available service information.
- `settings.yml`: Configuration file that defines the services and their settings (e.g., protocol, IP address, and port).
- `message.py`: Helper module containing utility functions for handling messages between client and server.
- `server.py`: The entry point for the discovery server application, which periodically broadcasts its own information to connected clients and receives service information from them.

## Usage

### Running the Client

To run the client, navigate to the project directory and execute:

```bash
python client.py
```

The client will continuously connect to the discovery server and display available services on your network.

### Running the Server

To run the server, navigate to the project directory and execute:

```bash
python server.py
```

The server will broadcast its own information periodically and receive service information from clients.

## Customization

Service information for the discovery server is defined in `settings.yml`. Modify this file to add, remove, or update services as needed.

Example:

```yaml
servers:
  - socialgames:
      proto: TCP
      ip: 0.0.0.0
      port: 4242
```

This configuration defines a single service called `socialgames`, using the TCP protocol on IP address `0.0.0.0` and port `4242`.

## Contributing

We welcome contributions from the community to help improve this project. Please see our [Contributing Guide](CONTRIBUTING.md) for more information on how to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

If you find `service_discover` useful, please consider starring the repository and sharing it with others!