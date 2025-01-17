# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import yaml
import json
import sys
import jsonschema
import pathlib

HEADER_LINE = (
    "// This file was generated by generate_feature_manifest.py from FeatureManifest.yaml."
    " DO NOT EDIT."
)

FEATURE_MANIFEST_SCHEMA = pathlib.Path(
    "schemas", "ExperimentFeatureManifest.schema.json"
)

EXPORTED_SYMBOLS = 'const EXPORTED_SYMBOLS = ["{}"];'


def write_fm_js_headers(fd):
    fd.write("\n".join([HEADER_LINE, EXPORTED_SYMBOLS.format("FeatureManifest")]))


def generate_feature_manifest(fd, input_file):
    write_fm_js_headers(fd)
    nimbus_dir_path = pathlib.Path(input_file).parent
    try:
        with open(input_file, "r") as yaml_input:
            data = yaml.safe_load(yaml_input)
            with pathlib.Path(nimbus_dir_path, FEATURE_MANIFEST_SCHEMA).open() as f:
                schema = json.load(f)
                for feature_entry in data:
                    try:
                        jsonschema.validate(data[feature_entry], schema)
                    except Exception as e:
                        print("Error while validating FeatureManifest.yaml")
                        print("On key: {}".format(feature_entry))
                        print("Input file: {}".format(input_file))
                        raise e
            fd.write("const FeatureManifest = {};".format(json.dumps(data)))
    except (IOError) as e:
        print("{}: error:\n  {}\n".format(input_file, e))
        sys.exit(1)
