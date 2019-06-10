from haystack.backends.elasticsearch2_backend import Elasticsearch2SearchBackend
from haystack.backends.elasticsearch2_backend import Elasticsearch2SearchEngine


class IKSearchBackend(Elasticsearch2SearchBackend):
    DEFAULT_ANALYZER = "ik_max_word"

    def __init__(self, connection_alias, **connection_options):
        super().__init__(connection_alias, **connection_options)

    def build_schema(self, fields):
        content_field_name, mapping = super(IKSearchBackend, self).build_schema(fields)
        for field_name, field_class in fields.items():
            field_mapping = mapping[field_class.index_fieldname]
            if field_mapping["type"] == "string" and field_class.indexed:
                if not hasattr(
                    field_class, "facet_for"
                ) and not field_class.field_type in ("ngram", "edge_ngram"):
                    field_mapping["analyzer"] = getattr(
                        field_class, "analyzer", self.DEFAULT_ANALYZER
                    )
            mapping.update({field_class.index_fieldname: field_mapping})
        return content_field_name, mapping


class IKSearchEngine(Elasticsearch2SearchEngine):
    backend = IKSearchBackend