// загружаем список проектов
export const fetchProjects = async ({commit, state}) => {
  const response = await fetch(`${state.apiUrlProjects}`);
  if (response.ok) {
    commit('projectsFetched', await response.json());

    // если загружаем впервые - устанавливаем выбранный проект
    if (!state.selectedProject && !!state.projects.length) commit('setSelectedProject', state.projects[0]);
  } else {
    commit('setAlarm', response);
  }
};
