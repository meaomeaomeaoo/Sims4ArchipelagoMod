from typing import Any, Dict

from sims4communitylib.persistence.data_stores.common_data_store import CommonDataStore


class S4APSettings:
    MOD_VERSION = 'mod_version'  # Fixed at time of first start
    SEED_NAME = 'seed_name'  # From RoomInfo and if set checked against it to prevent booting of multiple seeds per save
    HOST_NAME = 'host'  # From Login and if set checked against it to prevent booting of multiple seeds per save
    PORT_NUMBER = 'port'  # From Login and if set checked against it to prevent booting of multiple seeds per save
    PLAYER = 'player'  # From RoomInfo and if set checked against it to prevent booting of multiple seeds per save
    INDEX = 'index'  # Index received from ReceivedItems
    ITEMS = 'items'  # Items received from ReceivedItems
    ITEM_IDS = 'item_ids'  # Item ids received from ReceivedItems
    LOCATIONS = 'locations'  # The Locations for the received items in ReceivedItems
    SENDERS = 'senders'  # The players who sent the item
    GOAL = 'goal' # the goal of the game
    CAREER = 'career' # the chosen career for logic

class S4APGenericDataStore(CommonDataStore):
    """ Manager of generic stuff. """

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_identifier(cls) -> str:
        return 's4ap_generic_settings'

    # noinspection PyMissingOrEmptyDocstring
    @property
    def _version(self) -> int:
        # We specify a version so that when the data set changes we can force an update of the data set within the game of players.
        return 1

    # noinspection PyMissingOrEmptyDocstring
    @property
    def _default_data(self) -> Dict[str, Any]:
        # We specify the default values for our data within here.
        return {
            S4APSettings.MOD_VERSION: self._version,
            S4APSettings.SEED_NAME: None,
            S4APSettings.HOST_NAME: None,
            S4APSettings.PORT_NUMBER: 0,
            S4APSettings.PLAYER: None,
            S4APSettings.INDEX: None,
            S4APSettings.ITEMS: None,
            S4APSettings.ITEM_IDS: None,
            S4APSettings.LOCATIONS: None,
            S4APSettings.SENDERS: None,
            S4APSettings.GOAL: None,
            S4APSettings.CAREER: None,
        }.copy()
