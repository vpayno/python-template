# python-template

[![actionlint](https://github.com/vpayno/python-template/actions/workflows/actionlint.yaml/badge.svg?branch=main)](https://github.com/vpayno/python-template/actions/workflows/actionlint.yaml)
[![git](https://github.com/vpayno/python-template/actions/workflows/git.yaml/badge.svg?branch=main)](https://github.com/vpayno/python-template/actions/workflows/git.yaml)
[![json](https://github.com/vpayno/python-template/actions/workflows/json.yaml/badge.svg?branch=main)](https://github.com/vpayno/python-template/actions/workflows/json.yaml)
[![linkcheck](https://github.com/vpayno/python-template/actions/workflows/linkcheck.yaml/badge.svg?branch=main)](https://github.com/vpayno/python-template/actions/workflows/linkcheck.yaml)
[![markdown](https://github.com/vpayno/python-template/actions/workflows/markdown.yaml/badge.svg?branch=main)](https://github.com/vpayno/python-template/actions/workflows/markdown.yaml)
[![proselint](https://github.com/vpayno/python-template/actions/workflows/proselint.yaml/badge.svg?branch=main)](https://github.com/vpayno/python-template/actions/workflows/proselint.yaml)
[![spellcheck](https://github.com/vpayno/python-template/actions/workflows/spellcheck.yaml/badge.svg?branch=main)](https://github.com/vpayno/python-template/actions/workflows/spellcheck.yaml)
[![woke](https://github.com/vpayno/python-template/actions/workflows/woke.yaml/badge.svg?branch=main)](https://github.com/vpayno/python-template/actions/workflows/woke.yaml)
[![yaml](https://github.com/vpayno/python-template/actions/workflows/yaml.yaml/badge.svg?branch=main)](https://github.com/vpayno/python-template/actions/workflows/yaml.yaml)

[![python](https://github.com/vpayno/python-template/actions/workflows/python.yaml/badge.svg?branch=main)](https://github.com/vpayno/python-template/actions/workflows/python.yaml)
[![python-dependency-update](https://github.com/vpayno/python-template/actions/workflows/python-dependency-update.yaml/badge.svg?branch=main)](https://github.com/vpayno/python-template/actions/workflows/python-dependency-update.yaml)

My Python repo template.

## RunMe Playbook

This and other readme files in this repo are RunMe Playbooks.

Use this playbook step/task to update the [RunMe](https://runme.dev) cli.

If you don't have runme installed, you'll need to copy/paste the command. :)

```bash { background=false category=runme closeTerminalOnSuccess=true excludeFromRunAll=true interactive=true interpreter=bash name=setup-install-runme promptEnv=true terminalRows=10 }
go install github.com/stateful/runme/v3@v3
```

Install Playbook dependencies:

```bash { background=false category=runme closeTerminalOnSuccess=true excludeFromRunAll=true interactive=true interpreter=bash name=setup-runme-deps promptEnv=true terminalRows=10 }
go install github.com/charmbracelet/gum@latest
```

## Using PDM

- Installing PDM

Use this `runme` playbook task will either install or update `pdm`.

```bash { background=false category=setup closeTerminalOnSuccess=true excludeFromRunAll=true interactive=true interpreter=bash name=setup-pdm-install promptEnv=true terminalRows=10 }
set -ex

if [[ -z ${PYENV_ROOT} ]]; then
    pip install --user --upgrade pdm
else
    pip install --upgrade pdm
fi
printf "\n"
```

- Setup PDM

Use this `runme` playbook task to setup the project's virtual env.

```bash { background=false category=setup closeTerminalOnSuccess=true excludeFromRunAll=true interactive=true interpreter=bash name=setup-pdm-init promptEnv=true terminalRows=10 }
set -ex

if [[ ! -d .venv ]]; then
    # pdm venv create
    pdm use "$(which python)"
    printf "\n"
fi

pdm venv list
printf "\n"

pdm lock
printf "\n"

pdm sync
printf "\n"
```

- Using PDM's virtual env

Use this `runme` playbook task to sync the project's virtual env.

```bash { background=false category=setup closeTerminalOnSuccess=true excludeFromRunAll=true interactive=true interpreter=bash name=setup-pdm-sync promptEnv=true terminalRows=10 }
set -ex

if [[ ! -d .venv ]]; then
    pdm venv create
    printf "\n"
fi

pdm venv list
printf "\n"

pdm sync
printf "\n"
```

- Update project dependencies

Use this `runme` playbook task to update the projects dependencies.

```bash { background=false category=setup closeTerminalOnSuccess=true excludeFromRunAll=true interactive=true interpreter=bash name=setup-pdm-update-deps promptEnv=true terminalRows=10 }
set -ex

pdm sync
printf "\n"

pdm outdated
printf "\n"

pdm update
printf "\n"

git add pdm.lock
git commit -m 'chore: update dependencies'
git lg origin/main..
```
