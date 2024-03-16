To direct where the pods should be scheduled, we can label nodes with meaningful labels and then use node affinity in our StatefulSet to schedule the pods on the nodes with the appropriate labels.

## Labeling Nodes

We can label nodes using the kubectl label command. For example, to label a node, we can run the following command:

```bash
kubectl label nodes <node-name> <label-key>=<label-value>
```

For example, we can lable our nodes with the following labels:

```bash
kubectl label nodes <vm2-node-name> worker-node=vm2
kubectl label nodes <vm3-node-name> worker-node=vm3
```