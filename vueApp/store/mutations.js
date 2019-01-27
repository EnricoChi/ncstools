// обновляем спсиок проектов
export const projectsFetched = (state, data) => { state.projects = [ ...data ] };

// устанавливаем выбранный проект
export const setSelectedProject = (state, project) => { state.selectedProject = project };

// активируем сообщение об ошибке
export const setAlarm = (state, data) => {
  console.log('setAlarm ->\t', data)
};

// активируем окно диалога (Projects, Files, Features)
export const toggleDialog = (state, dialogName) => {
  state.dialogs[dialogName].show = !state.dialogs[dialogName].show;
};
