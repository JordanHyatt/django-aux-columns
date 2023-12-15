# django-aux-columns

Provides additional specialty column types to supplement the fantastic [django-tables2](https://django-tables2.readthedocs.io/en/latest/) library

#### Column List

* FixedTextColumn - Renders a fixed text (Allows mimicing the behavior of LinkedColumn)
* CheckFkColumn - Checks for the existance of a FK relationship
* RoundNumberColumn - Rounds numbers to a given precision and allows for formating
* CollapseDictColumn - Renders a dictionary in collapsable div
* CollapseDataFrameColumn - Renders a QS (or similar data) as a pandas DataFrame inside a collapsable div
* CollapseIterableColumn - Renders an iterable as a list inside a collapsable div
* CollapseNonIterableColumn - Renders a non-iterable (typically large text) inside a collapseable div
* BarChartColumn - Renders the column as a "bar-chart" similar to "Data Bars" in excel
* LastChangeDateColumn - Renders last change date of the record (only valid with django-simple-history)
* LastChangeDateColumn - Renders last change date of the record (only valid with django-simple-history)
* LastChangeType - Renders last change type of the record (only valid with django-simple-history)
