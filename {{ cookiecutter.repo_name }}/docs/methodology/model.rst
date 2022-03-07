Methodology
===========

ML use case overview
--------------------

* something like an overview of supervised Learning
* probably can be recycled from agency wide descriptions

Model overview
--------------

* Explain the model/modelling exercise
  * potentially reusable from other projects that used the same model(s)
* Assumptions behind the model
* iid observations
* future observation are coming from the same distribution of the dataset used
  to train the model

Model use case
--------------

* How was the model used to solve the problem
* Model specific preprocessing procedures
* Model trainig procedure
* Validation method

Evaluation protocol
-------------------

* Give precise specifications of the evaluation protocol you used to evaluate the 
  proposed methodology, including precise implementable mathematical definitions of the performance metrics you used. In other words, describe fully the procedure you used to obtain the performance metrics you reported, starting from raw data you used, but treating the proposed methodology as a black box. The description of the proposed methodology itself will appear in a later section. Note that, by following the evaluation protocol specifications, the methodology reviewer, at least in theory, should be able to reproduce the exact values of the performance metrics you obtained. Usually, one should evaluate at least how accurate (does it on average give correct inferences) and how stable (the extent to which individual estimates/predictions could deviate from true values) an inference procedure is.
* Suppose you knew–magically–the true values of the characteristics being 
  inferred. Give accordingly the ideal – though probably not implementable in practice – evaluation protocol for the proposed inference procedure, given the production context within which it is deployed.
* Describe the differences between the actual evaluation protocol and the ideal 
  one. Explain why the actual evaluation protocol is the closest possible to the ideal one, given operationally constraints.
* With respect to the differences between the actual evaluation protocol and the 
  ideal one, enumerate the
* assumptions under which the actual evaluation protocol remains valid and 
  relevant with respect to the use case in question.
* Give an assessment regarding the extent to which the aforementioned assumptions 
  actually hold in practice, within the context of the parent production process. In particular, justify the validity of these assumptions in practice if possible.

Model Monitoring
----------------

* Is there a mechanism in place or will there be a mechanism in place to track 
  performance metrics of the model through time? If so, describe the metric(s).
* Is there a mechanism in place to deal with non-stationary data?
* Is there a mechanism in place to track and deal with model drift?
