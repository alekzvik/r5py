#!/usr/bin/env python3

"""Wraps a com.conveyal.r5.api.util.LegMode enum set."""

import enum

import com.conveyal.r5


__all__ = ["LegMode"]


class LegMode(enum.Enum):
    WALK = com.conveyal.r5.api.util.LegMode.valueOf("WALK")
    BICYCLE = com.conveyal.r5.api.util.LegMode.valueOf("BICYCLE")
    CAR = com.conveyal.r5.api.util.LegMode.valueOf("CAR")
    BICYCLE_RENT = com.conveyal.r5.api.util.LegMode.valueOf("BICYCLE_RENT")
    CAR_PARK = com.conveyal.r5.api.util.LegMode.valueOf("CAR_PARK")
