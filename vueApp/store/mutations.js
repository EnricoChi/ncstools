export const toggleDialog = (state, dialog) => {
  switch (dialog) {
    case state.dialogProjects.name:
      state.dialogProjects.show = !state.dialogProjects.show; break;
    default: break;
  }
};
