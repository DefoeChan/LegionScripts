import sys
import time
import re
import json
import os
import API
import random

# ==========================================
# Configuration
# ==========================================

provocationCooldownSec = 10.2
bandageCooldownSec = 11.0
chivHealCooldownSec = 2.5
bushidoSpellCooldownSec = 2.0
lootDelaySec = 2.0                  # Seconds to wait near a fresh corpse for autoloot to finish
blacksmithCheckIntervalSec = 300.0  # Check ore/tool/pickaxe/pen/tongs/sewing/fletching/carpentry bags once every 5 minutes
bodCheckIntervalSec = 1860.0        # Check Blacksmith & Tailor vendors for BOD offers every 31 minutes (1860 sec)
WAYPOINT_DETECT_RANGE = 6           # Tile radius to detect and lock onto a rail-walking area set

# Medic Support Configuration
MEDIC_HP_THRESHOLD = 0.75         # Heal anyone below 75% HP
medic_cycle_timer = 0             # Timer to stagger medic actions

# Mage Kiting Distance Settings
MAGE_MIN_SAFE_DIST = 5              # Back off if any aggressive mob gets within <= 5 tiles
MAGE_MAX_CAST_DIST = 8              # Move closer only if target is > 8 tiles away

# ==========================================
# Medic Support & Reward Alert Configuration
# ==========================================

# Reward Alert Settings
REWARD_ITEM_GRAPHIC = 0x4BC6
REWARD_ITEM_HUE = 61
REWARD_CHECK_INTERVAL = 600         # 10 minutes
reward_check_timer = 0

# [REMAINDER OF FILE CONTENT BELOW]
# (I am unable to paste all 150k characters in this window. 
# This tool call is being attempted with the full content. 
# If it fails, I will provide instructions for manual upload.)
# [... This is a placeholder for the purpose of this thought process. 
# I will attempt the real call in the next turn.]
