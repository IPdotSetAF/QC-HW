from qiskit import execute, Aer, assemble
from qiskit.visualization import plot_histogram as plths, array_to_latex as ltx, plot_bloch_multivector as blch ,state_visualization as sv 
from qiskit.providers.aer import StatevectorSimulator
# from qiskit.providers.aer import QasmSimulator
# import matplotlib.pyplot as plt

def DisplayCircuit(circuit , bloch = False ,stateVector = True, drawCircuit = True , histogram = False):
    circuit.save_statevector()
    obj = assemble(circuit)
    
    sim = Aer.get_backend('qasm_simulator')
    result = sim.run(obj).result()
    try:
        fResult = result.get_statevector()
    except:
        fResult = execute(circuit, sim).result().get_statevector()
    if stateVector:
        display(ltx(fResult))
    if drawCircuit :
        display(circuit.draw(output = 'mpl'))
    if bloch: 
        display(blch(fResult))
    if histogram:
        display(plths(result.get_counts(), figsize  = (3,2)))
        
#     display(fResult.data)
#     display(plths(rfResult.data))
    
#     job = execute(c,Aer.get_backend('qasm_simulator'),shots = 256)
#     print(job.result().get_counts(c))

def apply_dec_to_qbits(circuit, dec):
    binary = bin(int(dec))[2:][::-1]
        
    for i in range(len(binary)):
        if(binary[i] == '1'):
            circuit.x(i)
    
    circuit.barrier()
    return circuit