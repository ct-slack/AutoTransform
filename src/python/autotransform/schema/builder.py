# AutoTransform
# Large scale, component based code modification library
#
# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2022-present Nathan Rockenbach <http://github.com/nathro>

# @black_format

"""The base class for SchemaBuilders which are used to programatically generate a Schema."""

from abc import ABC, abstractmethod
from typing import List, Optional

from autotransform.batcher.base import Batcher
from autotransform.batcher.single import SingleBatcher
from autotransform.command.base import Command
from autotransform.filter.base import Filter
from autotransform.input.base import Input
from autotransform.repo.base import Repo
from autotransform.schema.config import SchemaConfig
from autotransform.schema.schema import AutoTransformSchema
from autotransform.transformer.base import Transformer
from autotransform.validator.base import Validator


class SchemaBuilder(ABC):
    """The base for SchemaBuilders. SchemaBuilders are used for programatic Schema generation.
    This can be used in conjunction with params or configuration to customize Schemas run
    through automation. Can also be used to generate JSON Schemas that can be utilized.
    """

    @abstractmethod
    def get_input(self) -> Input:
        """Get the Input for the Schema.

        Returns:
            Input: The Input that will be used in the built Schema.
        """

    def get_filters(self) -> List[Filter]:
        """Get the Filters for the Schema.

        Returns:
            List[Filter]: The Filters that will be used in the built Schema.
        """

        # pylint: disable=no-self-use

        return []

    def get_batcher(self) -> Batcher:
        """Get the Batcher for the Schema.

        Returns:
            Batcher: The Batcher that will be used in the built Schema.
        """

        # pylint: disable=no-self-use

        return SingleBatcher(title="")

    @abstractmethod
    def get_transformer(self) -> Transformer:
        """Get the Transformer for the Schema.

        Returns:
            Transformer: The Transformer that will be used in the built Schema.
        """

    def get_validators(self) -> List[Validator]:
        """Get the Validators for the Schema.

        Returns:
            List[Validator]: The Validators that will be used in the built Schema.
        """

        # pylint: disable=no-self-use

        return []

    def get_commands(self) -> List[Command]:
        """Get the Commands for the Schema.

        Returns:
            List[Command]: The Commands that will be used in the built Schema.
        """

        # pylint: disable=no-self-use

        return []

    def get_repo(self) -> Optional[Repo]:
        """Get the Repo for the Schema.

        Returns:
            Repo: The Repo that will be used in the built Schema.
        """

        # pylint: disable=no-self-use

        return None

    def get_config(self) -> SchemaConfig:
        """Get the SchemaConfig for the Schema.

        Returns:
            SchemaConfig: The SchemaConfig that will be used in the built Schema.
        """

        # pylint: disable=no-self-use

        return SchemaConfig(type(self).__name__)

    def build(self) -> AutoTransformSchema:
        """Builds a Schema based on the state of the SchemaBuilder.

        Returns:
            AutoTransformSchema: The Schema produced by this SchemaBuilder.
        """

        return AutoTransformSchema(
            self.get_input(),
            self.get_batcher(),
            self.get_transformer(),
            filters=self.get_filters(),
            validators=self.get_validators(),
            commands=self.get_commands(),
            repo=self.get_repo(),
            config=self.get_config(),
        )

    def dump_to_file(self, path: str) -> None:
        """Dumps the Schema this SchemaBuilder would produce to the file located at the provided
        path.

        Args:
            path (str): The path of the file to dump the JSON encoded Schema to.
        """

        # pylint: disable=unspecified-encoding

        with open(path, "w") as file:
            file.write(self.build().to_json(pretty=True))
