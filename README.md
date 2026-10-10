# Weil positivity on the window of width log 15 — certificate data

Data for the interval-arithmetic certificate of: R. Mori, *Weil positivity on the window of width log 15*, Zenodo, 2026,
doi:10.5281/zenodo.XXXXXXXX (paper VIII). The code (checker, proposer, generator, independent check) is in folder
`certificate-VIII/` of https://github.com/moriryota/prolate-weil-bounds (release v1.6.0), doi:10.5281/zenodo.23092422.

Theorem O: for every complex C² function f supported in [−½ log 15, ½ log 15], Weil's quadratic form satisfies
Q(f) ≥ 2^−2904 ‖f‖². This is an external Arb/FLINT certificate together with an analytic proof, not a formal proof.

## Contents (about 1.8 GB)
| path | content |
|---|---|
| `notes/0803_gpt_A5_mu15_certificate/packet/p{0,1}_*.json.gz` | the certificate: 18 dyadic rational matrices (832 × 832, denominator 2^512) per parity: A, B, J, X, W0, Y and the congruence transforms ZC, ZW, ZT |
| `notes/0792_claude_lowmem_generator/runs/m15n1664p3328q224_p{0,1}_{A,B,J}.json.gz.partNN` | the six source matrices (Arb balls at 3328 bits), split into 48 MiB parts because GitHub limits files to 100 MB |
| `restore.py` | copies the packet, joins the parts, and checks every file against the SHA-256 sums shipped with the code |
| `SHA256SUMS` | SHA-256 of every file in this repository (parts included) |

The paths are those of the author's working tree, so that the hashes pinned inside the certificate remain valid.

## Use
    shasum -a 256 -c SHA256SUMS
    python restore.py /path/to/prolate-weil-bounds/certificate-VIII

then follow `certificate-VIII/README.md` (checker: about 200 s and 3.2 GB).

Licence: CC BY 4.0 (data), Apache-2.0 (`restore.py`).
