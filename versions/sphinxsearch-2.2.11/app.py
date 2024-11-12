from flask import Flask,request
import subprocess
import os

#
# Hacky way to re-index from another container.
#

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def status():
    if not 'SPHINX_VERIFY' in os.environ:
        return '[config error]'

    if os.environ['SPHINX_VERIFY'] != request.args.get('sphinx_verify'):
        return '[empty]'
    popen = subprocess.Popen(("/usr/local/bin/searchd", "--status"), stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    return output

@app.route("/", methods = ['POST'])
def reindex():
    if not 'SPHINX_VERIFY' in os.environ:
        return '[config error]'
    if os.environ['SPHINX_VERIFY'] != request.args.get('sphinx_verify'):
        return '[empty]'
    popen = subprocess.Popen(("/usr/local/bin/indexer", "--rotate", "--all"), stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    return output

