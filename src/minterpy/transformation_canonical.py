"""
Concrete implementations of the Transformation classes for the CanonicalPolynomial.

Transformations from Canonical basis to Newton and Lagrange basis are provided.
"""

from minterpy import CanonicalPolynomial
from minterpy.lagrange_polynomial import LagrangePolynomial
from minterpy.newton_polynomial import NewtonPolynomial
from minterpy.transformation_abstract import TransformationABC
from minterpy.transformation_utils import (
    _build_canonical_to_lagrange_operator, _build_canonical_to_newton_operator)

__all__ = ["TransformationCanonicalToNewton", "TransformationCanonicalToLagrange"]


class TransformationCanonicalToNewton(TransformationABC):
    """Transformation from CanonicalPolynomial to NewtonPolynomial
    """

    origin_type = CanonicalPolynomial
    target_type = NewtonPolynomial
    _get_transformation_operator = _build_canonical_to_newton_operator


class TransformationCanonicalToLagrange(TransformationABC):
    """Transformation from CanonicalPolynomial to LagrangePolynomial
    """

    origin_type = CanonicalPolynomial
    target_type = LagrangePolynomial
    _get_transformation_operator = _build_canonical_to_lagrange_operator
