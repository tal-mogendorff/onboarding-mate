# Onboarding Mate Tool

## Overview
The Onboarding Mate tool is designed to automate the process of onboarding new organizations to Kubiya. It provides a streamlined way to register new organizations and their administrators through a simple API call.

## Prerequisites
- Python 3.9 or higher
- Kubiya SDK installed (`pip install kubiya-sdk`)
- Valid Kubiya API key

## Installation

1. Install the required dependencies:
```bash
pip install kubiya-sdk
```

2. Set up your API key as an environment variable:
```bash
export KUBIYA_API_KEY='your-api-key-here'
```

## Tool Configuration
The tool is configured with the following parameters:

- **Name**: `onboarding_mate`
- **Description**: Onboard a new organization to Kubiya
- **Base Image**: `alpine/curl`
- **API Endpoint**: `https://api.kubiya.ai/api/v1/onboard`

### Required Arguments
1. `org_name` (string)
   - Description: The name of the organization to be onboarded
   - Required: Yes

2. `admin_email` (string)
   - Description: The email address of the organization administrator
   - Required: Yes

## Usage

### Python Implementation
```python
from kubiya_sdk.tools import Tool
from kubiya_sdk.tools.registry import tool_registry

# Import and use the tool
onboarding_mate = Tool(
    name="onboarding_mate",
    description="Onboard a new organization to Kubiya",
    image="alpine/curl",
    content="""curl -X POST https://api.kubiya.ai/api/v1/onboard \
    -H "Authorization: UserKey ${KUBIYA_API_KEY}" \
    -H "Content-Type: application/json" \
    -d '{
        "org_name": "'"${org_name}"'",
        "admin_email": "'"${admin_email}"'"
    }'""",
    secrets=["KUBIYA_API_KEY"],
    args=[
        {
            "name": "org_name",
            "description": "The name of the organization",
            "type": "str",
            "required": True,
        },
        {
            "name": "admin_email",
            "description": "The email of the organization admin",
            "type": "str",
            "required": True,
        },
    ],
)

# Register the tool
tool_registry.register("onboarding_mate", onboarding_mate)
```

### Example Usage
```python
# Example of how to use the tool
result = tool_registry.execute(
    "onboarding_mate",
    args={
        "org_name": "Example Corp",
        "admin_email": "admin@example.com"
    }
)
```

## API Response
The tool makes a POST request to the Kubiya API endpoint. A successful response will confirm the organization's onboarding.

## Security Considerations
- The API key should be kept secure and never committed to version control
- Use environment variables or secure secret management for the `KUBIYA_API_KEY`
- The tool uses HTTPS for secure communication with the API

## Error Handling
The tool will raise appropriate exceptions if:
- Required arguments are missing
- API key is not set
- API request fails
- Invalid input data is provided

## Support
For additional support or questions, please contact Kubiya support or refer to the official documentation.

## Contributing
To contribute to this tool, please follow the standard pull request process and ensure all tests pass before submitting.

## License
Please refer to the Kubiya license agreement for terms of use.
