# dotG Performance Management System (PMS)

**dotG** is a professional-grade, modern Performance Management System built on top of the Frappe Framework and Vue.js (using Frappe-UI).

It is designed to eliminate the "Operational Friction" and "Strategic Gaps" found in traditional, static HR software by treating performance as a continuous, dynamic dialogue rather than a yearly event.

## Features

- **Continuous Feedback & Nudges**: Peer-to-peer shoutouts and constructive tips with AI sentiment tagging.
- **Dedicated 1-on-1 Workspace**: Shared agendas, action item tracking, and carry-over functionality.
- **OKR Framework**: Transparent, top-down Objectives linked to measurable, automatically-updating Key Results.
- **Talent Strategy & 9-Box Grid**: Dynamic competency mapping and skill gap assessments.
- **Automated Appraisals**: Cycles that automatically generate reviews based on continuous tracking data.
- **Modern Vue SPA**: A stunning, glassmorphic "SaaS" interface for employees and managers to interact with daily, completely separate from Frappe Desk.

## Documentation

- [User Guide & Process Flow](docs/USER_GUIDE.md): Step-by-step instructions on how to set up OKRs, run 1-on-1s, and execute a full appraisal cycle.

## Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/sawan-dotG/dot_pms.git --branch main
bench install-app dot_pms
```

### Running the Frontend

The beautiful, mobile-first Employee UI is built with Vue.js. To run it locally:

```bash
cd apps/dot_pms/frontend
npm install
npm run dev
```

## Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/dot_pms
pre-commit install
```

## License

MIT
