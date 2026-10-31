# Learning Causal Dynamics and Reward Machines: A Framework for Faster Reinforcement Learning with Extended Temporal Tasks

Code for the paper by Hadi Partovi Aria, H. Kim, Shayan Meshkat Alsadat, Zhe Xu. International Conference on Computer, Control and Robotics (ICCCR), 2025.

Causal dynamics learning (CDL) with CMI-based inference removes action-irrelevant state dimensions, and a reward machine learned from traces encodes the temporally extended task. The agent then learns over the abstract state and the reward machine state.

## Layout

`chemical_env/` is the first case study: a 6x6 Chemical environment with four objects whose colors and shapes change through actions and a causal graph. Set parameters in `chemical_env/cdl/policy_params.json` and run `main_policy.py` from `chemical_env/cdl/`. Example parameter files are in `chemical_env/example_params/`.

`robotic_manipulation/` is the second case study: ten dice on a 6x6 grid where a movable red die with a lower number is stacked on one with a higher number. It runs the same way from `robotic_manipulation/cdl/`.

`reward_machine_learning/` is the joint inference of reward machines and policies (JIRP) used to learn the reward machine, for example `cd reward_machine_learning/src && python run1.py --algorithm=jirp --world=office`.

## Running

```bash
pip install -r requirements.txt
cd chemical_env/cdl && python main_policy.py
```

## Credits

The CDL part builds on Wang et al., "Causal Dynamics Learning for Task-Independent State Abstraction" (ICML 2022, https://github.com/wangzizhao/CausalDynamicsLearning). The reward machine learning part builds on the JIRP code from Xu et al. and includes the libalf library, which keeps its own GPL license (`gpl.txt` in its folder).

## Citation

```bibtex
@inproceedings{aria2025cdlrm,
  title = {Learning Causal Dynamics and Reward Machines: A Framework for Faster Reinforcement Learning with Extended Temporal Tasks},
  author = {Hadi Partovi Aria and H. Kim and Shayan Meshkat Alsadat and Zhe Xu},
  booktitle = {2025 5th International Conference on Computer, Control and Robotics (ICCCR)},
  year = {2025}
}
```

## License

MIT, see `LICENSE`.
