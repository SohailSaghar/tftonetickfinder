import pprint
import json

def augments_picture():
    strs = """<img src="//cdn.lolchess.gg/upload/images/items/BalancedBudget_1685601607-balanced-budget-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Balanced Budget
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Tahm Kench]
                                                                                                                                                                                [Draven]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">At the start of the next 4 rounds, Gain 4 Gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/BalancedBudget2_1685601625-balanced-budget-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Balanced Budget II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Tahm Kench]
                                                                                                                                                                                [Draven]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">At the start of the next 4 rounds, Gain 6 Gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/BalancedBudget3_1685601635-balanced-budget-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Balanced Budget III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Tahm Kench]
                                                                                                                                                                                [Draven]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">At the start of the next 4 rounds, Gain 10 Gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/BattleReady_1685601465-battle-ready-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Battle Ready
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Vladimir]
                                                                                                                                                                                [Master Yi]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your team deals 3% more damage and takes 3% less damage. </p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/BattleReadyII_1685601476-battle-ready-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Battle Ready II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Vladimir]
                                                                                                                                                                                [Master Yi]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your team deals 6% more damage and takes 6% less damage. </p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/BattleReadyIII_1685601485-battle-ready-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Battle Ready III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Vladimir]
                                                                                                                                                                                [Master Yi]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your team deals 8% more damage and takes 8% less damage. </p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/BigGrabBag_1685601074-grab-bag-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Big Grab Bag
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Urf]
                                                                                                                                                                                [Ezreal]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 2 random components, 8 gold, and a Reforger. </p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_Ascension_1685599036-ascension2.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Ascension
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Veigar]
                                                                                                                                                                                [Vladimir]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">After 15 seconds of combat, your units deal 45% more damage.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_Experience1_1685598955-knowledge-download-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Knowledge Download I
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Aurelion Sol]
                                                                                                                                                                                [Caitlyn]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 12 XP.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_Experience2_1685598961-knowledge-download-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Knowledge Download II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Aurelion Sol]
                                                                                                                                                                                [Caitlyn]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 22 XP.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_Experience3_1685598994-knowledge-download-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Knowledge Download III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Aurelion Sol]
                                                                                                                                                                                [Caitlyn]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 36 XP.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_FinalAscension_1685599102-ascension3.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Final Ascension
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Veigar]
                                                                                                                                                                                [Vladimir]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your units deal 15% more damage. After 15 seconds, this effect triples.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_LargeForge_1685598364-forge-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Large Forge
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ornn]
                                                                                                                                                                                [Bard]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain an Ornn Item Anvil and a Component Item Anvil.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_LargeForgePlus_1685596443-job_s-done-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Masterful Job
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ornn]
                                                                                                                                                                                [Bard]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain an Ornn Item Anvil and a Completed Item Anvil</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_MediumForge_1685598375-forge-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Medium Forge
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ornn]
                                                                                                                                                                                [Bard]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a Completed Item Anvil and 10 Gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_MediumForgePlus_1685596419-job_s-done-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Job Well Done
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ornn]
                                                                                                                                                                                [Bard]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a Completed Item Anvil and a Component Anvil.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_Money_1685597871-money-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Money!
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Tahm Kench]
                                                                                                                                                                                [Lee Sin]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 10 Gold. In 4 turns, gain 10 Gold again.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_Money2_1685597879-money-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Money Money!
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Tahm Kench]
                                                                                                                                                                                [Lee Sin]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 16 Gold. In 4 turns, gain 16 Gold again.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_Money3_1685597888-money-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Money Money Money!
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Tahm Kench]
                                                                                                                                                                                [Lee Sin]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 25 Gold. In 4 turns, gain 25 Gold again.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_PartialAscension_1685598205-ascension1.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Partial Ascension
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Veigar]
                                                                                                                                                                                [Vladimir]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">After 15 seconds of combat, your units deal 30% more damage.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_RollingForDays_1685598389-rolling-for-days-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Rolling For Days I
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Draven]
                                                                                                                                                                                [Caitlyn]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 10 free shop refreshes. These shop refreshes carry over between rounds.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_RollingForDays2_1685598399-rolling-for-days-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Rolling For Days II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Draven]
                                                                                                                                                                                [Caitlyn]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 15 free shop refreshes, These shop refreshes carry over between rounds.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_RollingForDays3_1685598413-rolling-for-days-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Rolling For Days III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Draven]
                                                                                                                                                                                [Caitlyn]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 25 free shop refreshes, These shop refreshes carry over between rounds.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_SmallForge_1685598288-forge-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Small Forge
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ornn]
                                                                                                                                                                                [Bard]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a Component Anvil and 6 Gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_SmallForgePlus_1685596432-job_s-done-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Job&#039;s Done
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ornn]
                                                                                                                                                                                [Bard]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 2 Component Anvils.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_TeamingUp1_1685599056-teaming-up-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Seeing Double I
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Twisted Fate]
                                                                                                                                                                                [Bard]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a random item made from 2 of the same component and 5 gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_TeamingUp2_1685599067-teaming-up-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Seeing Double II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Twisted Fate]
                                                                                                                                                                                [Bard]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a random item made from 2 of the same component and 8 gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_TeamingUp3_1685599074-teaming-up-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Seeing Double III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Twisted Fate]
                                                                                                                                                                                [Bard]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 2 random items made from 2 of the same component and 3 gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_TinyPower1_1685598686-tiny-power-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Tiny Power I
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Veigar]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your units gain 7% Attack Damage, Ability Power, and Attack Speed.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_TinyPower2_1685598693-tiny-power-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Tiny Power II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Veigar]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your units gains 10% Attack Damage, Ability Power, and Attack Speed.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_TinyPower3_1685598699-tiny-power-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Tiny Power III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Veigar]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your units gains 16% Attack Damage, Ability Power, and Attack Speed.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_WellEarnedComforts_1685599463-well-earned-comforts-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Well-Earned Comforts I
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ezreal]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your units gain 60 Health for each item equipped.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_WellEarnedComforts2_1685599469-well-earned-comforts-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Well-Earned Comforts II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ezreal]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your units gain 111 Health for each item equipped.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Commander_WellEarnedComforts3_1685599480-well-earned-comforts-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Well-Earned Comforts III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ezreal]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your units gain 120 Health and 8% Attack Speed for each item equipped.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/FinalGrabBag_1685601061-final-grab-bag-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Final Grab Bag
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Urf]
                                                                                                                                                                                [Pengu]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a random component, 12 gold, and a Reforger. </p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/FinalGrabBagPlus_1685601088-final-grab-bag-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Final Grab Bag II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Urf]
                                                                                                                                                                                [Pengu]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 2 random components, 15 gold, and a Magentic Remover. </p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/FinalGrabBagPlusPlus_1686622960-final-grab-bag-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Urf&#039;s Grab Bag
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Urf]
                                                                                                                                                                                [Pengu]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 2 random components, a Champion Duplicator, and a Spatula. </p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/GiantGrabBag_1685601105-grab-bag-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Giant Grab Bag
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Urf]
                                                                                                                                                                                [Ezreal]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 3 random components, 10 gold, and a Lesser Champion Duplicator. </p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/GottaGoFast_1685601298-gotta-go-fast-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Gotta Go Fast!
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Master Yi]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your team generates 10% more mana and moves 20% faster.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/GottaGoFastII_1685601315-gotta-go-fast-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Gotta Go Fast! II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Master Yi]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your team generates 25% more mana and moves 40% faster.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/GottaGoFastIII_1685601327-gotta-go-fast-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Gotta Go Fast!!! III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Master Yi]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your team generates 35% more mana and moves 50% faster.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/itemgrabbag1.tft_set6.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Item Grab Bag I
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Twisted Fate]
                                                                                                                                                                                [Pengu]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 1 random completed item.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/ItemGrabBagPlus_1685603718-itemgrabbag2.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Item Grab Bag II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Twisted Fate]
                                                                                                                                                                                [Pengu]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a random completed item, a random component, and 5 gold. </p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/ItemGrabBagPlusPlus_1685603734-itemgrabbag3.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Item Grab Bag III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Twisted Fate]
                                                                                                                                                                                [Pengu]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 2 random full items and 8 Gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/ItPaysToLearn_1686278406-it-pays-to-learn-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">It Pays To Learn
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Aurelion Sol]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 10 XP and 10 gold. </p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/ItPaysToLearnII_1686278415-it-pays-to-learn-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">It Pays to Learn II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Aurelion Sol]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 18 XP and 18 gold. </p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/ItPaysToLearnIII_1686278422-it-pays-to-learn-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">It Pays to Learn III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Aurelion Sol]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 24 XP and 24 gold. </p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_AFK_1685065046-afk-i.tft_set7.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">AFK
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Tahm Kench]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">You cannot perform actions for the next 3 rounds. Afterwards, gain 18 gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_BardPlaybook1_1685596377-caretaker_s-chosen-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Caretaker&#039;s Ally
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Bard]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Each time you level up, gain the same random Tier 2 champion.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_BardPlaybook2_1685596371-caretaker_s-chosen-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Caretaker&#039;s Favor
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Bard]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a component anvil when you reach level 5, 6, 7, and 8.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_BardPlaybook3_1685596365-caretaker_s-chosen-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Caretaker&#039;s Chosen
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Bard]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">As you level, gain more powerful items. At level 4 - gain a Component Anvil, at level 6 - gain a Completed Item Anvil, at level 7 - open a radiant item armory.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_BranchingOut_1685415054-Branching-Out-I.TFT_Set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Branching Out
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Urf]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a random Emblem and a Reforger.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_BuildingACollection_1685599167-buried-treasures-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Buried Treasures I
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ezreal]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a random item component at the start of the next 2 rounds. Now starts granting items the round the augment is selected.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_BuildingACollectionPlus_1685599172-buried-treasures-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Buried Treasures II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ezreal]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a random item component at the start of the next 3 rounds. Now starts granting items the round the augment is selected.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_BuildingACollectionPlusPlus_1685599179-buried-treasures-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Buried Treasures III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ezreal]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a random item component at the start of the next 5 rounds. Now starts granting items the round the augment is selected.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_CuttingCorners_1685949953-cutting-corners-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Cutting Corners
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Aurelion Sol]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Leveling up costs 3 XP less. You can now reach Level 10.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_DravenSpoilsOfWar_1686272255-spoils-of-war-legend-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Spoils of War I
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Draven]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">When you kill an enemy unit, there&#039;s a 25% chance to drop loot.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_DravenSpoilsOfWar2_1686272260-spoils-of-war-legend-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Spoils of War II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Draven]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">When you kill an enemy unit, there&#039;s a 30% chance to drop loot.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_DravenSpoilsOfWar3_1686272265-spoils-of-war-legend-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Spoils of War III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Draven]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">When you kill an enemy unit, there&#039;s a 40% chance to drop amazing loot.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_GreaterJeweledLotus_1685598037-jeweled-lotus-iii.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Jeweled Lotus III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Veigar]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your units&#039; Abilities can critically strike. Your units gain 45% Critical Strike chance.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_HedgeFund_1685415642-Hedge-Fund-III.TFT_Set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Hedge Fund
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Tahm Kench]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">You have no interest cap. Gain 16 gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_HighEndSector_1685599428-trade3.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Shopping spree
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Lee Sin]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 1 gold per round. When you level up, gain a number of free shop refreshes equal to your level, which carry over your rounds.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_JeweledLotus_1685064920-jeweled-lotus-ii.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Jeweled Lotus II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Veigar]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your units&#039; Abilities can critically strike. Your units gain 10% Critical Strike chance.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_LearningFromExperience2_1685935081-learning-from-experience-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Patient Study
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Aurelion Sol]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">After player combat, gain 2 XP if you won or 3 XP if you lost. You can now reach Level 10.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_LesserJeweledLotus_1685598018-jeweled-lotus-i.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Jeweled Lotus I
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Veigar]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Combat Start: Your strongest unit gains 25% critical strike chance and their spells can critically strike.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_LivingForge_1685064750-living-forge-iii.tft_set7.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Living Forge
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ornn]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain an Ornn Item Anvil now and after every 10 player combats.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_LongTimeCrafting_1685598918-long-time-crafting-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Latent Forge
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ornn]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain an Ornn Item Anvil after 8 player combats.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_MaxLevel10_1685064966-levelup3.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Level Up!
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Aurelion Sol]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">When you buy XP, gain an additional 3. Gain 4 immediately. You can now reach level 10.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_MetabolicAccelerator_1685064497-metabolicaccel2.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Metabolic Accelerator
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Pengu]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your Tactician moves faster and heals 2 Health after a PvP round.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_OnARoll_1685415164-On-a-Roll-I.TFT_Set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">On a Roll
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Lee Sin]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Whenever you star-up a champion, gain a free shop refresh.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_OneTwosThree_1686618788-OneTwosThree_1686277287-threes-company-i.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">One Twos Three
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Caitlyn]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 1 Tier one unit, 2 Tier two units, and 1 Tier three unit.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_PandorasItems_1685065136-pandora1.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Pandora&#039;s Items
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Twisted Fate]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a random component. Round Start: items on your bench are randomized (excluding Tactician&#039;s Crown, Spatula, and consumables).</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_PandorasItems2_1685599230-pandora2.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Pandora&#039;s Items II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Twisted Fate]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 1 completed item. Round Start: items on your bench are randomized (excluding Tactician&#039;s Crown, Spatula, and consumables).</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_PandorasRadiantBox_1685599187-pandora3.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Pandora&#039;s Box
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Twisted Fate]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a random Radiant item. Round Start: items on your bench are randomized (excluding Tactician&#039;s Crown, Spatula, and consumables).</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_PortableForge_1685064737-portableforge2.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Portable Forge
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Ornn]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Open an Armory and choose 1 of 3 unique Artifacts crafted by Ornn.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_PumpingUp_1685596334-pumping-up-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Pumping Up I
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Master Yi]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your units gain 8% Attack Speed. Each round, increase this by 0.5%. (current Attack Speed: %)</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_PumpingUp2_1685596340-pumping-up-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Pumping Up II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Master Yi]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your units gain 10% Attack Speed. Each round, increase this by 1%. (current Attack Speed: %)</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_PumpingUp3_1685596346-pumping-up-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Pumping Up III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Master Yi]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your units gain 10% Attack Speed. Each round, increase this by 2%. (current Attack Speed: %)</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_RichGetRicher_1685064998-richgetricher2.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Rich Get Richer
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Tahm Kench]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 12 gold. Your maximum interest is increased to 7.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_StarsAreBorn_1685415114-Stars-are-born-II.TFT_Set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Stars are Born
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Caitlyn]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">The first tier 1 unit and tier 2 unit you buy are upgraded to 2-star. Gain a 6 gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_StarterKit_1685415855-Starter-Kit-III.TFT_Set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Starter Kit
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Caitlyn]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a Tier 4 champion, and a 2-star Tier 2 champion that shares a trait with them. At the next 1 stages, gain the Tier 4 champion again.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_TiniestTitan_1685598619-tiniest-titaniii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Tiniest Titan
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Pengu]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your tactician is small and speedy, heals 2 Health after a PVP round, and grants 2 Gold per round.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_TinyTitans_1685064795-tiny-titans-i.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Tiny Titans
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Pengu]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your Tactician heals 30 Health, grows larger, and has 130 maximum Health.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_TomeOfTraits1_1685064677-ancientarchives2.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Ancient Archives I
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Urf]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 1 Tome of Traits and 5 gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_TomeOfTraits2_1685064682-ancientarchives3.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Ancient Archives II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Urf]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 2 Tome of Traits and 3 gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_TradeSector_1685064881-trade2.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Trade Sector
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Lee Sin]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a free Shop refresh each round. Gain a 2 gold.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_Transfusion_1685598483-transfusion-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Transfusion I
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Vladimir]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your team gains 20 Health, plus 2 Health per missing Tactician Health.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_TransfusionPlus_1685598490-transfusion-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Transfusion II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Vladimir]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your team gains 80 Health, plus 3 Health per missing Tactician Health.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/Legend_TransfusionPlusPlus_1685598496-transfusion-iii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Transfusion III
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Vladimir]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Your team gains 100 Health, plus 5 Health per missing Tactician Health.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/TinyGrabBag_1685601043-grab-bag-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Tiny Grab Bag
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Urf]
                                                                                                                                                                                [Ezreal]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain a random component, 4 gold, a Magnetic Remover. </p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/TopDeck_1685601699-training-reward-i.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Training Reward
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Lee Sin]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 7 gold and a Lesser Champion Duplicator.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/TopDeckPlus_1685601715-training-reward-ii.tft_set9.png" alt="" class="guide-augments__image">
                                <div class="guide-augments__content">
                                    <h3 class="guide-augments__title">Training Reward II
                                                                                                                    </h3>
                                    <p class="guide-augments__desc">
                                                                                                                                    [Lee Sin]
                                                                                                                        </p>
                                    <p class="guide-augments__desc">Gain 15 gold and a Lesser Champion Duplicator.</p>
                                </div>
                            </div>
                                                    <div class="guide-augments">
                                <img src="//cdn.lolchess.gg/upload/images/items/TopDeckPlusPlus_1685601734-training-reward-iii.tft_set9.png" alt="" class="guide-augments__image">""".split('<img src="//cdn.lolchess.gg/upload/images/items/')
    for i in strs:
        print(i.split("\"")[0][i.split("\"")[0].find("-")+1:len(i)])
def tftaugment_json():
    with open("tft-augments.json", "r", encoding="utf-8") as file:
        text = json.load(file)

        for i in text['data']:
            print(text['data'][i])


def imagenames():
    strs = """balanced-budget-i.tft_set9.png
balanced-budget-ii.tft_set9.png
balanced-budget-iii.tft_set9.png
battle-ready-i.tft_set9.png
battle-ready-ii.tft_set9.png
battle-ready-iii.tft_set9.png
grab-bag-ii.tft_set9.png
ascension2.png
knowledge-download-i.tft_set9.png
knowledge-download-ii.tft_set9.png
knowledge-download-iii.tft_set9.png
ascension3.png
forge-iii.tft_set9.png
job_s-done-iii.tft_set9.png
forge-ii.tft_set9.png
job_s-done-ii.tft_set9.png
money-i.tft_set9.png
money-ii.tft_set9.png
money-iii.tft_set9.png
ascension1.png
rolling-for-days-i.tft_set9.png
rolling-for-days-ii.tft_set9.png
rolling-for-days-iii.tft_set9.png
forge-i.tft_set9.png
job_s-done-i.tft_set9.png
teaming-up-i.tft_set9.png
teaming-up-ii.tft_set9.png
teaming-up-iii.tft_set9.png
tiny-power-i.tft_set9.png
tiny-power-ii.tft_set9.png
tiny-power-iii.tft_set9.png
well-earned-comforts-i.tft_set9.png
well-earned-comforts-ii.tft_set9.png
well-earned-comforts-iii.tft_set9.png
final-grab-bag-i.tft_set9.png
final-grab-bag-ii.tft_set9.png
final-grab-bag-iii.tft_set9.png
grab-bag-iii.tft_set9.png
gotta-go-fast-i.tft_set9.png
gotta-go-fast-ii.tft_set9.png
gotta-go-fast-iii.tft_set9.png
itemgrabbag1.tft_set6.png
itemgrabbag2.png
itemgrabbag3.png
it-pays-to-learn-i.tft_set9.png
it-pays-to-learn-ii.tft_set9.png
it-pays-to-learn-iii.tft_set9.png
afk-i.tft_set7.png
caretaker_s-chosen-i.tft_set9.png
caretaker_s-chosen-ii.tft_set9.png
caretaker_s-chosen-iii.tft_set9.png
Branching-Out-I.TFT_Set9.png
buried-treasures-i.tft_set9.png
buried-treasures-ii.tft_set9.png
buried-treasures-iii.tft_set9.png
cutting-corners-i.tft_set9.png
spoils-of-war-legend-i.tft_set9.png
spoils-of-war-legend-ii.tft_set9.png
spoils-of-war-legend-iii.tft_set9.png
jeweled-lotus-iii.png
Hedge-Fund-III.TFT_Set9.png
trade3.png
jeweled-lotus-ii.png
learning-from-experience-ii.tft_set9.png
jeweled-lotus-i.png
living-forge-iii.tft_set7.png
long-time-crafting-i.tft_set9.png
levelup3.png
metabolicaccel2.png
On-a-Roll-I.TFT_Set9.png
OneTwosThree_1686277287-threes-company-i.png
pandora1.png
pandora2.png
pandora3.png
portableforge2.png
pumping-up-i.tft_set9.png
pumping-up-ii.tft_set9.png
pumping-up-iii.tft_set9.png
richgetricher2.png
Stars-are-born-II.TFT_Set9.png
Starter-Kit-III.TFT_Set9.png
tiniest-titaniii.tft_set9.png
tiny-titans-i.png
ancientarchives2.png
ancientarchives3.png
trade2.png
transfusion-i.tft_set9.png
transfusion-ii.tft_set9.png
transfusion-iii.tft_set9.png
grab-bag-i.tft_set9.png
training-reward-i.tft_set9.png
training-reward-ii.tft_set9.png
training-reward-iii.tft_set9.png""".split("\n")
    for i in strs:
        print(i)


if __name__ == '__main__':
    imagenames()