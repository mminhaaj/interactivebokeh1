set-psdebug -trace 2

function test() {
    conda install --quiet $(python scripts/deps.py run test).split()
    bokeh sampledata
}

test
