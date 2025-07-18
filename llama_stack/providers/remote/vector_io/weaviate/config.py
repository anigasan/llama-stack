# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Any

from pydantic import BaseModel, Field

from llama_stack.providers.utils.kvstore.config import (
    KVStoreConfig,
    SqliteKVStoreConfig,
)


class WeaviateRequestProviderData(BaseModel):
    weaviate_api_key: str
    weaviate_cluster_url: str
    kvstore: KVStoreConfig | None = Field(description="Config for KV store backend (SQLite only for now)", default=None)


class WeaviateVectorIOConfig(BaseModel):
    @classmethod
    def sample_run_config(cls, __distro_dir__: str, **kwargs: Any) -> dict[str, Any]:
        return {
            "kvstore": SqliteKVStoreConfig.sample_run_config(
                __distro_dir__=__distro_dir__,
                db_name="weaviate_registry.db",
            ),
        }
