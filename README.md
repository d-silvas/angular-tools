# Angular tools

Tools for an Angular project

## duplicate_actions.py

Run this script to find duplicate action types among your action files. The script assumes that
- All action files end with `actions.ts`.
- You write your action types in an enum, with the following format:
```typescript
export enum FeatureActionTypes {
    actionOne = '[Feature] Action One',
    actionTwo = '[Feature] Action Two',
}

export const actionOne = createAction(FeatureActionTypes.actionOne);
```

The script walks over every folder under `./src`, finds duplicate action names, and writes them
in a new file called `duplicate_actions.json`.
