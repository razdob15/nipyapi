# -*- coding: utf-8 -*-

"""
For interactions with the NiFi Canvas
"""

from __future__ import absolute_import
from swagger_client import ControllerApi, SystemdiagnosticsApi


def get_system_diagnostics():
    """
    Returns NiFi Sytems diagnostics page
    :return JSON object:
    """
    return SystemdiagnosticsApi().get_system_diagnostics()


def get_cluster():
    """
    Returns the contents of the NiFi cluster
    :return:
    """
    return ControllerApi().get_cluster()


def get_node(nid):
    """
    Returns the cluster node information
    :param nid: NiFi ID (nid) from Node information
    :return:
    """
    return ControllerApi().get_node(nid)
