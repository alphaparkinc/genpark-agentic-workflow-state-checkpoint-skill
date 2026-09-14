import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AgenticWorkflowStateCheckpointClient

def main():
    client = AgenticWorkflowStateCheckpointClient()
    # Step 1
    c1 = client.commit_state_checkpoint("sess_01", "STEP_CART_CREATED", {"cart_id": "c1", "items": ["S8_MAXV"]})
    print(f"Checkpoint 1: {c1['checkpoint_id']} ({c1['status']})")
    # Step 2
    c2 = client.commit_state_checkpoint("sess_01", "STEP_INVENTORY_LOCKED", {"cart_id": "c1", "locked": True})
    print(f"Checkpoint 2: {c2['checkpoint_id']} | Rollback Target: {c2['safe_rollback_target']}")
    print(f"Total Checkpoints: {c2['total_checkpoints_in_session']}")

if __name__ == '__main__':
    main()
