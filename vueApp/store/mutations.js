// обновляем спсиок проектов
export const projectsFetched = (state, data) => { state.projects = [ ...data ] };

// устанавливаем выбранный проект
export const setSelectedProject = (state, project) => { state.selectedProject = project };

// активируем сообщение об ошибке
export const setAlarm = (state, data) => {
  console.log('setAlarm ->\t', data)
};

// активируем окно диалога (Projects, Files, Features)
export const toggleDialog = (state, dialog) => {
  switch (dialog) {
    case state.dialogProjects.name:
      state.dialogProjects.show = !state.dialogProjects.show; break;
    default: break;
  }
};
