# HIL-QUADS

Project Overview:

QUADS stands for quick and dirty scheduler, an opensource project developed by Red Hat that helps in machine allocation based on various policies. It uses date/time based YAML schedule for machine allocations and has support for automated visualization of current and future allocations. QUADS is used on a daily basis in Red Hat Systems Design and Engineering group to test and vet Red Hat products at scale.

HIL , or the Hardware Isolation Layer, is a minimalistic layer that decouples node allocation from node provisioning. It allows mutually untrusting physically deployed services to share the data center while resources can move back and forth between them. HIL is used in production on a daily basis in the MOC.

QUADS is independent of the underlying provisioning system and HIL does not put restrictions on how the nodes are scheduled. In this project, you will extend QUADS to schedule resources allocated using HIL. Success will enable developers to perform large scale experiments on physical hardware allocated out of the MOC. You can expect this service to be used by researchers and students from MIT, Harvard, BU, NU and UMass, as well as Open Source developers and the industry partners of the MOC.

You will learn in depth about scheduling, provisioning, and complexity of integrating existing systems to create a new solution with a chance to get your pull requests integrated into QUADS and HIL. You will analyze and make modifications to the code-base of both of these projects. If needed you will develop new API calls. This will include a full cycle of development experience from proposing the design, implementation and unit testing to documentations for users and developers.

Workflow for QUADS:

 * redhat-performance/quads (Gerrit Requests)
   * BUEC528-HIL-QUADS/quads (Pull Requests)
     * isaac/quads (work)
     * dan/quads (work)
     * etc. (other student repos)
