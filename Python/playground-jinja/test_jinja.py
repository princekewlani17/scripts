#! /Users/princekewlani/.pyenv/versions/3.12.4/bin/python3

# System Lib Imports
import os
import datetime
import pytz

# Third Party Lib Imports
from jinja2 import Environment, FileSystemLoader

# Global Vars
OUTPUT_DIR="outputs"


def generate_body_with_normal_params(msg, region, tmpl_name):
    environment = Environment(
        loader=FileSystemLoader(f"{os.path.dirname(__file__)}/templates/")
    )

    template = environment.get_template(tmpl_name)
    content = template.render(
        message=msg,
        region=region,
        time=datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S'),
    )
    return content, tmpl_name


def generate_body_with_json_params(msg, region, tmpl_name):
    environment = Environment(
        loader=FileSystemLoader(f"{os.path.dirname(__file__)}/templates/")
    )

    template = environment.get_template(tmpl_name)
    
    data = {
        'Region': region,
        'Time': datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S'),
        'Info': 'test template'
    }
    
    content = template.render(
        message=msg,
        data=data
    )
    return content, tmpl_name


os.makedirs(f"{os.path.dirname(__file__)}/{OUTPUT_DIR}", exist_ok=True)
for out_file, tmpl_name in [
    generate_body_with_normal_params(msg="Hello, Test!",
                                     region="ap-south-1",
                                     tmpl_name="example_template_normal_params.html"),
    generate_body_with_json_params(msg="Hello, Test!",
                                   region="ap-south-1",
                                   tmpl_name="example_template_json_params.html")
    ]:
    with open(f"{os.path.dirname(__file__)}/outputs/output.{tmpl_name}", "w") as outfile:
        outfile.write(out_file)

exit(0)
