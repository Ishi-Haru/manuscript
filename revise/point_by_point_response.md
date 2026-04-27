# Reviewer Comments

## Reviewer 1

<span style="color: #57ACFB; ">
1. The prefactor C of equation 2 has units of length and is given by C=0.41 nm
</span>

Thank you for pointing this out. We revised the manuscript to clarify that the prefactor \(C\) in Eq. 2 has dimensions of length. We now write the MD-based value as \(C = \SI{0.41}{\nano\metre}\) and have added units to all occurrences of the scaling prefactor \(C\) in the manuscript and Supporting Information, including the figure captions and comparison table.

Changes:
Clarified in the main text that \(C\) is a prefactor with dimensions of length.
Updated all occurrences of \(C = 0.41\) and \(C = 6.0\) for the scaling law in the manuscript and Supporting Information to include nanometer units.

<span style="color: #57ACFB; ">
2. The scaling law in equation 2 was derived for non-polar surfaces that interact with water only via dispersion or Lennard-Jones interactions, that means that hydrophilic surfaces were created by large dispersion attraction. In the recent publication “Subnanometer Interfacial Hydrodynamics: Spatially Resolved Viscosity and Surface Friction”, Carlson et al., Nano Lett. 2025, 25, 15605−15612 MD simulations were used to model polar surfaces where small contact angles are created by polar surface groups, which is more realistic. The fit of the friction coefficient is for these systems better represented by a exponential, not by a power law. For the non-polar surfaces the authors are mostly interested this does not make a difference, but for future studies this could be relevant.
</span>

Thank you for this helpful comment. We agree that Eq. 2 was originally derived for non-polar, dispersion-dominated surfaces and that polar surfaces can exhibit different relationships between wettability and interfacial friction, as reported by Carlson et al. In the present work, Eq. 2 is used as a reference scaling law for comparing our experimentally measured slip lengths, and our main conclusions are based on the direct slip-length measurements on flat surfaces and on the distinct behavior of HOPG. Therefore, this point does not affect the conclusions of the manuscript, but it is an important consideration for future studies of polar surfaces.

Changes:
No changes were made to the manuscript.

## Reviewer 2

<span style="color: #57ACFB; ">
1. Firstly, the title of the paper is currently not wholly accurate. The word "Does" should be replaced with "Need", i.e., the title should be "Water Need Not Slip on Hydrophobic Surfaces: Insights from Slip Length Mapping". This is because water does slip on graphite, so the authors cannot generally state that water does not slip on hydrophobic surfaces. Instead, the claim should be that water need not slip on hydrophobic surfaces.
</span>

Thank you for this helpful suggestion. 

Changes:
変更なし

<span style="color: #57ACFB; ">
2. The authors need to contextualize their results vis-a-vis those of Secchi et al. (https://www.nature.com/articles/nature19315), who found massive radius-dependent water slippage in carbon nanotubes (CNTs), with slip lengths on the order of hundreds of nanometers. The authors should explain why there is massive slippage on CNTs but not on the surfaces they examined.
</span>

Thank you for this important suggestion. We have added a discussion that explicitly compares our planar-surface measurements with the CNT results reported by Secchi et al. We now clarify that the massive, radius-dependent slippage inside CNTs does not contradict our results on nanoscopically flat planar surfaces. Secchi et al. themselves noted that slip lengths inside CNTs are consistently much larger than those measured on planar hydrophobic and graphite surfaces, where the slip length is typically at most a few tens of nanometers. We therefore distinguish the planar graphite slip regime observed here from the confinement-induced CNT transport regime, in which nanotube curvature and cylindrical confinement can further reduce water--carbon friction.

Changes:
Added a new paragraph in the discussion section comparing the present planar HOPG result with Secchi et al.'s CNT slippage results.
Added Secchi et al. as a new reference in the manuscript.

<span style="color: #57ACFB; ">
3. The derivation of eq. 3 and 4 must be provided along with the paper and the symbol hdot must be explained in the main text, including how it is measured experimentally.
</span>

Thank you for pointing this out. We have revised the main text to clarify the origin of Eqs. 3 and 4 and to define \(\dot{h}\). Equation 3 is the lubrication-theory expression for the hydrodynamic force between a sphere and a plane with slip boundary conditions, and we now explicitly cite Vinogradova for this result. Because the full derivation is lengthy, we refer readers to the original theoretical work. For Eq. 4, the derivation is already provided in the Supporting Information; we have added a concise explanation in the main text that it follows from \(\gamma_{\text{total}}=\gamma_{\text{tip}}+\gamma_{\text{bulk}}\), \(Q=k/(\omega\gamma_{\text{total}})\), and the proportionality \(A\propto Q\) under constant drive power. We also now define \(\dot{h}\) as the time derivative of the measured probe-substrate distance \(h(t)\), calculated numerically from the measured \(h(t)\) data.

Changes:
Clarified in the main text that Eq. 3 is based on the lubrication-theory result of Vinogradova for a sphere-plane geometry with slip boundary conditions.
Added the definition and experimental determination of \(\dot{h}\) in the main text.
Added a concise derivation route for Eq. 4 in the main text and pointed to the Supporting Information for details.

<span style="color: #57ACFB; ">
4. The authors mention that the "Slip length bs is then obtained by fitting Eq. 5 to a damping-coefficient-tip-sample distance curve with bs as the fitting parameter." However, the functional form of f* in Eq. 5 is not provided, making it unclear as to how bs can be extracted. This omission must be clarified and the form of f* must be derived and mentioned in the paper.
</span>

Thank you for pointing out this omission. We have revised the main text to explicitly provide the functional form of the correction factor \(f^*\) used in Eq. 5. The revised manuscript now gives \(f^*(h,b_t,b_s)\) together with the auxiliary quantities \(A\), \(B\), and \(C\).

Changes:
Added the explicit functional form of \(f^*(h,b_t,b_s)\) to the main text.
Defined the auxiliary quantities \(A\), \(B\), and \(C\) used in \(f^*\).
Updated the notation from \(f^*(b_t,b_s)\) to \(f^*(h,b_t,b_s)\) in the relevant equations.

<span style="color: #57ACFB; ">
5. For the fit in Figure 2a, please provide the goodness of fit (R^2) or any other metric, such as the mean absolute error, to quantify how good the fit is. Also, the authors must explain as to how error bars were obtained on the reported slip lengths. Are these confidence intervals from the fit, or standard deviations/errors from repeated measurements?
</span>

Thank you for this helpful suggestion. We have added goodness-of-fit metrics for the representative fit in Fig. 2a. The fitted curve gives \(R^2 = 0.6631\) and a mean absolute error of \(\SI{0.0141}{\micro\newton\second\per\metre}\). In addition, we clarified that the error bars in Fig. 4 are standard deviations of the slip lengths obtained from the \(128 \times 128\) pixels in each slip-length map, rather than confidence intervals from a single fit or standard errors.

Changes:
Added \(R^2\) and mean absolute error for the fit shown in Fig. 2a.
Clarified the interpretation of the goodness-of-fit metrics in the main text.
Clarified in the Fig. 4 caption that the error bars are standard deviations calculated from the \(128 \times 128\) pixel-wise slip-length values in each map.

<span style="color: #57ACFB; ">
6. The authors state that "We calibrated the slip length of the probe tip by measuring a symmetric system (bt = bs) using an atmospheric-plasma-treated diamond-like carbon (DLC) substrate, yielding a slip length of bt = bs = 0.0 ±1.2 nm." The authors should show the fit plot for this case, similar to what they did in Figure 2a.
</span>

Thank you for this suggestion. We have added a representative fitting plot for the tip slip-length calibration on the atmospheric-plasma-treated DLC substrate to the Supporting Information. The added figure shows the measured damping coefficient, the no-slip curve, and the fitted curve, and the mean absolute error of this representative fit was \(\SI{0.016}{\micro\newton\second\per\metre}\). We have also revised the main text to explicitly refer to this Supporting Information figure when discussing the calibration of the probe-tip slip length.

Changes:
Added a representative DLC calibration fitting plot to the Supporting Information.
Reported the mean absolute error of the representative DLC calibration fit in the Supporting Information caption.
Added a main-text reference to the new Supporting Information figure.

<span style="color: #57ACFB; ">
7. Plots should also be shown for the fit used to extract the slip length of 345.3 nm above the nanobubble, as mentioned towards the end of page 8.
</span>

Thank you for pointing this out. We have added a representative fitting plot for the nanobubble slip-length extraction to the Supporting Information. The added figure shows the measured damping coefficient directly above the nanobubble, together with the no-slip curve and the fitted curve, and the mean absolute error of this representative fit was \(\SI{0.014}{\micro\newton\second\per\metre}\). We have also revised the main text to refer to this Supporting Information figure where the nanobubble slip length of \(345.3 \pm \SI{23.7}{\nano\metre}\) is discussed.

Changes:
Added a representative nanobubble fitting plot to the Supporting Information.
Reported the mean absolute error of the representative nanobubble fit in the Supporting Information caption.
Added a main-text reference to the new Supporting Information figure.

<span style="color: #57ACFB; ">
8. Why are negative slip lengths obtained on the flat silica and FOPA regions? What is the physical meaning of a negative slip length? Isn't the lowest value of the slip length 0?
</span>

Thank you for raising this point. We have clarified the meaning of the small negative slip lengths obtained on the flat silica and FOPA regions. A negative slip length formally means that the extrapolated zero-velocity plane lies on the liquid side of the geometrical solid-liquid interface. While subnanometer negative slip may arise from molecular-scale effects such as adsorbed ions or immobilized hydration layers, we do not interpret the present values of \(-0.7 \pm \SI{0.6}{\nano\metre}\) and \(-0.9 \pm \SI{0.6}{\nano\metre}\) as physically meaningful large negative slip lengths. Instead, these small offsets likely arise from the propagation of systematic uncertainties in parameters such as the probe radius, spring constant, distance origin, and background damping into the fitted slip length. Importantly, these uncertainties are far smaller than the tens-of-nanometers slip observed on HOPG, so they do not affect our conclusion that the flat silica and FOPA regions exhibit a no-slip boundary condition.

Changes:
Added an explanation of the formal meaning of negative slip length.
Clarified that the small negative values measured on silica and FOPA are interpreted as no-slip within systematic uncertainty, not as physically meaningful large negative slip.
Explained that the uncertainty is much smaller than the slip length observed on HOPG and therefore does not affect the main conclusion.

<span style="color: #57ACFB; ">
9. Why is the water slip length 0.8 nm on Teflon but 43.2 on HOPG, despite Teflon expected to have a higher contact angle of water than HOPG?
</span>

Thank you for raising this important point. We have revised the discussion to explicitly compare Teflon and HOPG. We now clarify that the larger slip length on HOPG does not arise from higher hydrophobicity. Contact angle is a macroscopic measure of wettability, whereas slip length is controlled by interfacial friction. After noting that atomic-scale chemical heterogeneity can create a more corrugated interfacial energy landscape and increase water-solid friction, we explain that Teflon, although more hydrophobic, is a polymeric surface with molecular-scale conformational and chemical heterogeneity. This contrast supports our conclusion that true slip length on flat surfaces is governed more strongly by atomic-scale structure and chemical homogeneity than by contact angle alone.

Changes:
Added an explicit comparison between Teflon and HOPG in the discussion.
Clarified that macroscopic wettability alone does not determine slip length.
Emphasized the role of atomic-scale smoothness, crystallinity, and chemical homogeneity in reducing water-solid friction.

<span style="color: #57ACFB; ">
10. Figure 4 presents a systematic comparison of slip lengths on nanoscopically flat substrates. How is it proved that these surfaces are nanoscopically flat? The authors need to provide some proof using AFM measurements.
</span>

Thank you for this suggestion. We have revised the manuscript to make the evidence for nanoscopic flatness more explicit. AFM topography maps for the nanoscopically flat substrates are already provided in Fig. S of the Supporting Information, together with the corresponding slip-length maps. We have now revised the Fig. 4 caption to explicitly direct readers to these topography data and the measured nanoscale roughness values. The measured \(R_a\) values were \(\SI{0.27}{\nano\metre}\), \(\SI{0.29}{\nano\metre}\), \(\SI{0.64}{\nano\metre}\), and \(\SI{0.35}{\nano\metre}\) for mica, FDTS, Teflon, and HOPG, respectively, confirming that these substrates are nanoscopically flat.

Changes:
Revised the Fig. 4 caption to explicitly refer to the Supporting Information topography maps.
Clarified that the Supporting Information figure includes measured nanoscale roughness values.
Used the AFM topography data to support the statement that the substrates are nanoscopically flat.

<span style="color: #57ACFB; ">
11. For eq. 2, the units of b must be specified for completeness. The authors also must provide a table of the calculated b (from eq. 2) and the measured b from their experiments for all the surfaces examined in this work.
</span>

<span style="color: #57ACFB; ">
12. How can the authors claim that a water contact angle of 120 degrees is the near-maximum achievable on a topographically smooth flat surface? Ref. 21 mentions that "This value is considered to be the lowest surface free energy of any solid, based on the hexagonal closed alignment of −CF3 groups on the surface." Thus, for surfaces with other than CF3 groups, the contact angle could be higher. Also, the presence of CF3 groups would make the surface topographically rough, as compared to say, graphite.
</span>

Thank you for this careful comment. We agree that \(\SI{120}{\degree}\) should not be described as an absolute maximum contact angle for all possible surfaces. We have revised the wording to clarify that \(\SI{120}{\degree}\) is used as a representative upper-range value for chemically homogeneous smooth flat surfaces when roughness-induced Cassie states are not involved. The revised text now notes that low-surface-energy fluorinated surfaces, including PTFE and densely packed \(-\mathrm{CF}_3\)-terminated surfaces, typically approach this value, whereas much larger apparent contact angles generally require micro/nanoscale roughness and Cassie-state wetting. We also revised the Fig. 4 caption accordingly and added the relevant references.

Changes:
Revised the main-text statement so that \(\SI{120}{\degree}\) is not presented as an absolute maximum.
Clarified that larger apparent contact angles generally require roughness-induced Cassie states rather than surface chemistry alone.
Added references to Quere and Verho et al. to support this clarification.
Revised the Fig. 4 caption to describe the gray region as an approximate upper range for chemically homogeneous smooth flat surfaces.

<span style="color: #57ACFB; ">
13. The authors mention that "The contact angles of deionized-water droplets, measured separately on the hydrophilic and hydrophobic surfaces, were 28◦ and 105◦, respectively." How quickly were these measurements done since exposure to the atmosphere can change the contact angle, particularly for hydrophilic surfaces?
</span>

Thank you for raising this point. We have revised the manuscript to clarify how the contact angles of the hydrophilic and hydrophobic regions were measured. Because the patterned regions in the composite substrate were too small for direct droplet measurements, we prepared reference hydrophilic and hydrophobic substrates using the same processes as those used for the corresponding regions of the composite substrate. Their contact angles were measured immediately before the FM-AFM measurements. This procedure minimized possible changes caused by atmospheric exposure, particularly for the hydrophilic surface, and the measured values are therefore expected to represent the contact angles of the corresponding regions during slip-length mapping. We also added this detail to the Supporting Information.

Changes:
Clarified in the main text that contact angles were measured on reference substrates prepared by the same process as the composite substrate.
Specified that the contact-angle measurements were performed immediately before the FM-AFM measurements.
Added the corresponding procedural detail to the Supporting Information.

<span style="color: #57ACFB; ">
14. The authors need to substantiate the claim that "compared with hydrophilic surfaces (i.e., contact angles <90 degree), there is no clear consensus on slip lengths for hydrophobic surfaces (i.e., contact angles > 90 degree)." They should also state what consensus there is in the field for hydrophilic surfaces, along with providing suitable references.
</span>

Thank you for pointing this out. We have revised the introduction to substantiate this statement more explicitly. The revised text now states that reported slip lengths on hydrophilic smooth surfaces are generally close to zero within experimental uncertainty, whereas values reported for hydrophobic surfaces scatter widely from near-zero to tens or even hundreds of nanometers, as summarized in Fig. 1. We also clarified that previous studies have attributed large apparent slip on hydrophobic surfaces to several different origins, including surface roughness, nanobubbles, and measurement artifacts. This explains why a clear consensus has not yet been reached regarding the intrinsic slip length on hydrophobic surfaces.

Changes:
Clarified the consensus that hydrophilic smooth surfaces generally exhibit no-slip or near-no-slip behavior within experimental uncertainty.
Used the broad scatter in the literature data summarized in Fig. 1 as evidence for the lack of consensus on hydrophobic surfaces.
Added a sentence noting that large apparent slip on hydrophobic surfaces has been attributed to multiple origins, including roughness, nanobubbles, and measurement artifacts.

<span style="color: #57ACFB; ">
15. Pristine graphite is actually hydrophilic as revealed in the last decade (https://pubs.acs.org/doi/full/10.1021/acs.accounts.6b00447). How do the authors then explain the relatively large water slip length seen on HOPG in their measurements? Is it due to hydrophobic molecules adsorbed on the surface, or due to nanobubbles, as they have speculated in some other cases in the paper?
</span>

[x] checked

Thank you for raising this important point. We revised the discussion to clarify the origin of the large slip length observed on HOPG while focusing on the contact angle measured in this study. The HOPG surface was freshly cleaved immediately before measurement and showed only moderate wettability (\(\SI{59.0}{\degree}\)), so the large slip length is unlikely to originate primarily from hydrophobic adsorbates, whose accumulation on graphitic surfaces has been reported to occur over longer time scales. We also clarified that the nanobubble observed in the HOPG map was a localized feature and was analyzed separately. Therefore, we attribute the slip length on the flat HOPG terrace to the low-friction graphite-water interface. Previous MD studies have reported the uniqueness of graphite: its atomic-scale smoothness drastically reduces friction, leading to the slip length on the order of \(\SI{50}{\nano\metre}\).

[ ] checked

Changes:
Revised the HOPG discussion to focus on the contact angle measured in this study rather than on the general wettability of pristine graphite.
Clarified that hydrophobic adsorbates are unlikely to be the primary origin of the large HOPG slip length because the HOPG surface was freshly cleaved immediately before measurement and showed only moderate wettability.
Clarified that the localized nanobubble was analyzed separately and is not the origin of the slip length on the flat HOPG terrace.
Added that the large slip length on the flat HOPG terrace is attributed to the low-friction graphite-water interface, consistent with MD studies reporting graphite slip lengths on the order of \(\SI{50}{\nano\metre}\).