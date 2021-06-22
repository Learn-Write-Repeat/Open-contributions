# Deep Residual Learning for Image Recognition Paper Review

This paper introduces Residual Nets (ResNets), which was the winning submission (152-layer deep) at ILSVRC 2015 and MS-COCO 2015, and achieves a top-5 error rate
of 3.57% (ensemble of two nets).

Deeper networks are harder to optimize for approximating identity mapping by multiple non-linear layers, they face the degradation problem,
i.e. higher training and test error than shallower nets. They address this issue by requiring solvers to memorize residual functions,
such as f(x) = H(x) - x, and by introducing shortcut connections. The learned weights should drive f(x) to 0 if identity mapping is the best formulation
(and they observe that this is suitable preconditioning as most residual function responses are small). Additional parameters are not required for shortcut 
connections (for identity mapping).Zero paddings (no parameters) or projections are used to change the size. Projections add more variables to the equation 
and perform slightly better. Bottleneck design, i.e. 1x1 convolutional layers before and after 3x3 convolutions to reduce and increase dimensions,
is used to further reduce computational complexity. They use ResNets in the Faster-RCNN setting for detection and localization tasks.

## Stregth of Paper
<li>ResNets are significantly deeper and more accurate than VGG while being significantly less computationally expensive.
Previous state-of-the-art ensembles are outperformed by a single ResNet. Their winning entry is a network ensemble made up of two networks.</li>

## Weakness of Paper
Many of the findings and design decisions are worthy of further investigation and deliberation.
Why do shortcuts skip the first two or three layers? What happens to performance if the number of layers skipped is increased?

What is the compatibility of shortcut connections with Inception modules?
Does performance improve if the statistical principles underlying both of these architectures are orthogonal?

Paper link:  https://arxiv.org/abs/1512.03385

By Hemaraj Dhakal





