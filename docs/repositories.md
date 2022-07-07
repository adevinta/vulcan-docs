# Repositories

This page contains a list of all public repositories related to Vulcan.

## Vulcan Core

Components necessary for running scans and processing results.

- [Vulcan Agent](https://github.com/adevinta/vulcan-agent): Runs and monitors check containers. Retrieves and pushes results.
- [Vulcan Checks](https://github.com/adevinta/vulcan-checks): Code, manifest and container images for every available Vulcan check.
- [Vulcan Scan Engine](https://github.com/adevinta/vulcan-scan-engine): Creates checks in a queue from a scan. Monitors the status of the scan.
- [Vulcan Persistence](https://github.com/adevinta/vulcan-persistence): Inventory of the deployed checks, default options and required variables.
- [Vulcan Check SDK](https://github.com/adevinta/vulcan-check-sdk): Development kit in Go language to create checks. Common functions.
- [Vulcan Build System](https://github.com/adevinta/vulcan-checks-bsys): Tool to build, test, compare and deploy check container images.
- [Vulcan Stream](https://github.com/adevinta/vulcan-stream): WebSockets stream to push commands from the scan engine to the agents.
- [Vulcan Report](https://github.com/adevinta/vulcan-report): Package in Go that exposes the Vulcan report format data model.
- [Vulcan Results](https://github.com/adevinta/vulcan-results): Service used to upload and store check results from the agents.

### Vulcan Core Tools

Components that are not part with Vulcan Core but work with Vulcan Core.

- [Vulcan Local](https://github.com/adevinta/vulcan-local): Tool to run Vulcan checks locally and as part of CI/CD pipelines.
- [Vulcan Core CLI](https://github.com/adevinta/vulcan-core-cli): Tool that intereacts with the Scan Engine to launch a Vulcan scan.
- [Security Overview](https://github.com/adevinta/security-overview): Tool that generates a static HTML report from a Vulcan scan.
- [Vulcan Groupie](https://github.com/adevinta/vulcan-groupie): Library used by the Security Overview to group similar vulnerabilities.

### Vulcan Checks

Components that are used by one or more Vulcan checks.

- [Restuss](https://github.com/adevinta/restuss): A client in Go for the Tenable API. Extended fork of the unmaintained [Restuss](https://github.com/stefanoj3/restuss).

## Vulcan API 

Components that allow users to interact with Vulcan and the data it generates.

- [Vulcan API](https://github.com/adevinta/vulcan-api): Manages users, teams, assets, policies and programs. Acts as an API gateway.
- [Vulnerability DB](https://github.com/adevinta/vulnerability-db): Stores detected findings, affected targets. Tracks status, calculates metrics.
- [Vulnerability DB API](https://github.com/adevinta/vulnerability-db-api): Exposes the data stored in the Vulnerability DB through a REST API.
- [Vulcan Reports Generator](https://github.com/adevinta/vulcan-reports-generator): Generates and sends all kinds of reports from Vulcan data.
- [Vulcan Crontinuous](https://github.com/adevinta/vulcan-crontinuous): Triggers periodic scans according to the scan program schedule.
- [Vulcan Types](https://github.com/adevinta/vulcan-types): Go package to determine the type of an asset through different means.
- [Errors](https://github.com/adevinta/errors): Go package to wrap and enrich errors in the Vulcan API.

## Vulcan Infrastructure

Components that are used to build and deploy Vulcan.

- [Vulcan Gitops](https://github.com/adevinta/vulcan-gitops): Basic information and scripts to deploy Vulcan in Kuberenetes.
- [Vulcan Charts](https://github.com/adevinta/vulcan-charts): Helm charts used to deploy Vulcan in Kubernetes.
- [Vulcan Checks Deploy](https://github.com/adevinta/vulcan-checks-deploy): Travis job definition to build and deploy checks.
- [Vulcan CI/CD](https://github.com/adevinta/vulcan-cicd): Old repository pending to be deprecated.

