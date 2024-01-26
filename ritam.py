import os
import argparse

# Define command-line arguments
parser = argparse.ArgumentParser(description="Generate Serenity configuration")
parser.add_argument("--build", default="LT Serenity mac", help="Build information")
parser.add_argument("--test-name", default="Your Test Name", help="Name of the test")
parser.add_argument("--video", default=True, type=bool, help="Enable video recording")
parser.add_argument("--network", default=True, type=bool, help="Enable network logs")
parser.add_argument("--console", default=True, type=bool, help="Enable console logs")
parser.add_argument("--visual", default=True, type=bool, help="Enable visual logs")
parser.add_argument("--page-load-timeout", type=int, default=30000, help="Page load timeout in milliseconds")
parser.add_argument("--script-timeout", type=int, default=30000, help="Script execution timeout in milliseconds")
parser.add_argument("--implicitly-wait-timeout", type=int, default=5000, help="Implicit wait timeout in milliseconds")

# Parse command-line arguments
args = parser.parse_args()

# Specify the full path for the configuration file
config_file_path = os.path.join("src", "test", "resources", "serenity.conf")

# Construct the configuration based on command-line arguments
config_content = f"""
serenity {{
  take.screenshots = FOR_FAILURES
  test.root = "starter.acceptancetests"
  logging = VERBOSE
}}

headless.mode = false
webdriver {{
  driver = remote

  remote.url="https://shubhamr:dl8Y8as59i1YyGZZUeLF897aCFvIDmaKkUU1e6RgBmlgMLIIhh@hub.lambdatest.com/wd/hub"

  capabilities {{
    browserName = "chrome"
    platformName = "Windows 11"

    "LT:options" {{
      build = "{args.build}"
      name = "{args.test_name}"
      video = {args.video}
      network = {args.network}
      console = {args.console}
      visual = {args.visual}
      bypassCommands={{"/alert/text": true}}
      "w3c" = true
    }}

    timeouts {{
      pageLoadTimeout = {args.page_load_timeout}
      scriptTimeout = {args.script_timeout}
      implicitlyWaitTimeout = {args.implicitly_wait_timeout}
    }}

    // Add any other Selenium capabilities that you need
  }}
}}
"""

# Save to serenity.conf
with open(config_file_path, "w") as config_file:
    config_file.write(config_content)

print(f"Serenity configuration has been written to '{config_file_path}'")
