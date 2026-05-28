Feature: CLI Entrypoint

  The command-line interface is the primary entry point for users interacting
  with the application. It handles argument parsing, help output, version
  display, and graceful error handling for unrecognised arguments.

  Rule: Help output
    When a user requests help via the --help flag, the application displays
    the application name, tagline, and a list of available commands and flags.
    The output is human-readable and exits with code 0.

    Behavior hints:
    - --help displays app name and tagline
    - --help lists available flags

  Rule: Version output
    When a user requests version via the --version flag, the application
    displays the application name and version string from package metadata.
    The output exits with code 0.

    Behavior hints:
    - --version displays app name and version string
    - --version output matches package metadata

  Rule: Unrecognised arguments
    When a user provides unrecognised flags or arguments, the application
    displays an error message and exits with code 2. When no arguments are
    provided, the application exits with code 0.

    Behavior hints:
    - Unknown flag exits with code 2
    - No arguments exits with code 0
