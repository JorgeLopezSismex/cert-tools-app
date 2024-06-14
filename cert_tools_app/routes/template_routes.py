import os
import sys
import argparse
import cert_tools

from flask import Blueprint, jsonify
from cert_tools.create_v2_certificate_template import create_certificate_template

template_bp = Blueprint('template_bp', __name__)

@template_bp.route('/', methods=['GET'])
def get_templates():
    products = [
        {"id": 1, "name": "Product 1"},
        {"id": 2, "name": "Product 2"}
    ]
    return jsonify(products)

@template_bp.route('/', methods=['POST'])
def create_template():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    print(project_root)
    
    try:
        certificate_details = {
            'badge_id': 'ssasda',
            'abs_data_dir': '/app/cert_tools_app/test/',
            'cert_image_file': 'image.jpg',
            'issuer_logo_file': 'logo.jpg',
            'certificate_title': 'SISMEX123',
            'certificate_description': '',
            'issuer_name': 'sdfsdfsfsdf',
            'issuer_email': 'jalopez@sismex.com',
            'revocation_list': 'sfsfsfsdfd',
            'criteria_narrative': 'sfsdfsddf',
            'issuer_signature_lines': [],
            'issuer_public_key': 'sfsfsdfsd',
            'display_html': 'sdfsdfsfsdfsdfsdfsd',
            'hash_emails': [],
            'issuer_id': '123',
            'issuer_url': 'sdfsfs',
            'additional_global_fields': [],
            'additional_per_recipient_fields': []
            }
        
        args = argparse.Namespace(**certificate_details)
        
        certificate_template = create_certificate_template(args)
        
        print(certificate_template)
        
        return jsonify(certificate_template)
    
    except TypeError as e:
        return jsonify("Type error occurred:", e)
    except AttributeError as e:
        return jsonify("Function or attribute not found:", e)
    except Exception as e:
        return jsonify("An error occurred:", e)