-- macros/cast_is_delayed.sql
{% macro cast_is_delayed(column_name) %}
    {% if target.name == 'production' %}
        -- In production, cast to STRING
        CAST({{ column_name }} AS STRING)
    {% else %}
        -- In dev or other environments, keep it as INT64
        {{ column_name }}
    {% endif %}
{% endmacro %}
