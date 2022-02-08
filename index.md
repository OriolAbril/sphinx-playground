# Playground home

Grid with dark/light only elements

::::{grid} 3
:::{grid-item-card}
Regular element
:::
:::{grid-item-card}
:class-item: only-light

only-light
:::
:::{grid-item-card}
Regular element 2
^^^

This element has a header and a body to test extra behaviour
and alignment of grid items of different size, but
it has no special classes and should be shown in both cases.
:::
:::{grid-item-card}
:class-item: only-dark

only-dark
:::
:::{grid-item-card}
Regular element 3
:::
::::

Grid with no special elements

::::{grid} 3
:::{grid-item-card}
Regular element
:::
:::{grid-item-card}
Regular element 2
^^^

This element has a header and a body to test extra behaviour
and alignment of grid items of different size, but
it has no special classes and should be shown in both cases.
:::
:::{grid-item-card}
Regular item 2.5
:::
:::{grid-item-card}
Regular element 3
:::
::::
