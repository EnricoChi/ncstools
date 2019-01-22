export const fetchProjects = async ({commit, state}) => {
  const response = await fetch(`${state.apiUrlProjects}`);
  console.log('fetchProjects ->\t', response)
};
