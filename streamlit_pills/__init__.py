from pathlib import Path
from typing import Iterable, Union

import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component("pills", url="http://localhost:3001")
else:
    path = (Path(__file__).parent / "frontend" / "build").resolve()
    _component_func = components.declare_component("pills", path=path)


def pills(
    label: str,
    options: Iterable[str],
    icons: Iterable[str] = None,
    index: Union[int, None] = 0,
    *,
    clearable: bool = None,
    key: str = None,
):
    """Shows clickable pills.

    Args:
        label (str): The label shown above the pills.
        options (iterable of str): The texts shown inside of the pills.
        icons (iterable of str, optional): The emoji icons shown on the left side of the
            pills. Each item must be a single emoji. Default to None.
        index (int or None, optional): The index of the pill that is selected by default.
            If None, no pill is selected. Defaults to 0.
        clearable (bool, optional): Whether the user can unselect the selected pill by
            clicking on it. If None, this is possible if `index` is set to None.
            Defaults to None.
        key (str, optional): The key of the component. Defaults to None.

    Returns:
        (any): The text of the pill selected by the user (same value as in `options`).
    """

    # Do some checks to verify the input.
    if len(options) < 1:
        raise ValueError("At least one option must be passed but `options` is empty.")
    if icons is not None and len(options) != len(icons):
        raise ValueError(
            "The number of options and icons must be equal but `options` has "
            f"{len(options)} elements and `icons` has {len(icons)} elements."
        )
    if index is not None and index >= len(options):
        raise ValueError(
            f"`index` must be smaller than the number of options ({len(options)}) "
            f"but it is {index}."
        )
    # TODO: Verify that icons are actually emoji icons.

    if clearable is None and index is None:
        clearable = True

    # Pass everything to the frontend.
    component_value = _component_func(
        label=label,
        options=options,
        icons=icons,
        index=index,
        clearable=clearable,
        key=key,
        default=index,
    )

    # The frontend component returns the index of the selected pill but we want to
    # return the actual value of it.
    if component_value is None or component_value == "None":
        return None
    else:
        return options[component_value]
