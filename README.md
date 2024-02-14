A much more detailed explanation of this project can be found at Presuppositions.pdf file in this repository

1 Problem statement:

My project’s central goal is to enhance the rea- soning inference capabilities of language models through the identification and integration of pre- suppositions from textual data.
Presuppositions are assumptions or inferences that are implicitly suggested in a statement or question. Identifying and understanding these can be crucial for a language model to fully grasp the context and implications of a sentence, leading to more accurate and nuanced responses.
My research is motivated by the observation that most language models, while performing well on a surface level, often miss out on these nuanced presuppositions, which can lead to mistakes in in- terpretation and subsequent reasoning tasks. Also, a presupposition is actually a valid data instance that includes true world knowledge and a coher- ent structure like all other sentences, so generating presupposition may help to generate more data if there is not enough data to train.
To address this, I’m proposing a two-model system:

a) A model responsible for identifying both static and contextual presuppositions from the sen- tences in a dataset. This model is actually a prompt engineering module that uses gpt-3.5-turbo. I in- structed it in order to:

1) Presupposition generated must be significantly different from original sentence.
2) Chosen presuppositions should give best information about the external world or situation that the sentence occured

b) A language model that will be fed by presup- positions.

My research aims to push the boundaries of lan- guage models’ inference capabilities by exploring and leveraging the often-overlooked aspect of pre- suppositions in textual data.

