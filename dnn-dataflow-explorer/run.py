import os
import pytimeloop.timeloopfe.v4 as tl

BASE = os.path.dirname(os.path.abspath(__file__))

spec = tl.Specification.from_yaml_files(
    os.path.join(BASE, "architectures/arch_4x4.yaml"),
    os.path.join(BASE, "workloads/resnet50_conv3x3.yaml"),
    os.path.join(BASE, "mappings/mapper.yaml"),
    os.path.join(BASE, "mappings/ws_4x4.yaml"),
)

tl.call_mapper(
    spec,
    output_dir=os.path.join(BASE, "results_4x4_ws")
)

print("\n=== DONE ===")
