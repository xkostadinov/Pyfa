# shipBonusRole2ArmorPlates&ShieldExtendersBonus
#
# Used by:
# Ships from group: Titan (6 of 6)
type = "passive"


def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Hull Upgrades"), "armorHPBonusAdd",
                                  src.getModifiedItemAttr("shipBonusRole2"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Upgrades"), "capacityBonus",
                                  src.getModifiedItemAttr("shipBonusRole2"))
