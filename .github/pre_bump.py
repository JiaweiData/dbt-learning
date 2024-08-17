import os
import tomlkit
from ruamel.yaml import YAML

def read_version_from_cz_toml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        cz_config = tomlkit.parse(f.read())
    return cz_config['tool']['commitizen']['version']

def update_version_in_dbt_project(file_path, version):
    yaml = YAML()
    yaml.preserve_quotes = True

    with open(file_path, 'r', encoding='utf-8') as f:
        dbt_project_config = yaml.load(f)

    dbt_project_config['version'] = version

    with open(file_path, 'w', encoding='utf-8') as f:
        yaml.dump(dbt_project_config, f)

def update_overview(source_path, target_path, version):
    # Replace %version% in overview.md.template
    with open(source_path, 'r', encoding='utf-8') as f:
        overview_content = f.read()

    overview_content = overview_content.replace('%version%', version)

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(overview_content)
def main():
    # 获取当前脚本所在的目录，然后找到上级目录
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    cz_toml_path = os.path.join(base_path, '.cz.toml')
    dbt_project_path = os.path.join(base_path, 'dbt_project.yml')

    version = read_version_from_cz_toml(cz_toml_path)
    update_version_in_dbt_project(dbt_project_path, version)

    print(f"Updated dbt_project.yml to version {version}")

    overview_template_path = os.path.join(base_path, 'docs', 'overview.md.template')
    overview_output_path = os.path.join(base_path, 'docs', 'overview.md')

    update_overview(overview_template_path, overview_output_path, version)
    print(f"Updated overview.md to version {version}")

if __name__ == '__main__':
    main()
