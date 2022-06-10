# AutoTransform
# Large scale, component based code modification library
#
# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2022-present Nathan Rockenbach <http://github.com/nathro>

# @black_format

"""Tests that the SchemaNameCondition works as expected."""

import mock
import pytest

from autotransform.change.base import Change
from autotransform.schema.config import SchemaConfig
from autotransform.schema.schema import AutoTransformSchema
from autotransform.step.condition.comparison import ComparisonType
from autotransform.step.condition.schema import SchemaNameCondition


def test_non_used_comparisons():
    """Checks that all unused comparisons assert as expected."""

    mock_config = mock.create_autospec(SchemaConfig)
    mock_config.schema_name = "foo"
    mock_schema = mock.create_autospec(AutoTransformSchema)
    mock_schema.config = mock_config
    mock_change = mock.create_autospec(Change)
    mock_change.get_schema.return_value = mock_schema

    condition = SchemaNameCondition(schema_name="foo", comparison=ComparisonType.GREATER_THAN)
    with pytest.raises(
        AssertionError, match="SchemaNameCondition may only use equal or not_equal comparison"
    ):
        condition.check(mock_change)

    condition = SchemaNameCondition(
        schema_name="foo", comparison=ComparisonType.GREATER_THAN_OR_EQUAL
    )
    with pytest.raises(
        AssertionError, match="SchemaNameCondition may only use equal or not_equal comparison"
    ):
        condition.check(mock_change)

    condition = SchemaNameCondition(schema_name="foo", comparison=ComparisonType.LESS_THAN)
    with pytest.raises(
        AssertionError, match="SchemaNameCondition may only use equal or not_equal comparison"
    ):
        condition.check(mock_change)

    condition = SchemaNameCondition(schema_name="foo", comparison=ComparisonType.LESS_THAN_OR_EQUAL)
    with pytest.raises(
        AssertionError, match="SchemaNameCondition may only use equal or not_equal comparison"
    ):
        condition.check(mock_change)
