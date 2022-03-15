<template>
    <div class="home">
        <h1 class="title">VUEAPP</h1>

        <hr>
        
        <div class="columns">
            <div class="column is-3 is-offset-3">
                <form>
                    <h2 class="subtitle">ADD TASK</h2>

                    <div class="field">
                        <label class="label">DESCRIPTION</label>
                        <div class="control">
                            <input class="input" type="text">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">STATUS</label>
                        <div class="control">
                            <div class="select">
                                <select>
                                    <option value="TODO"></option>
                                    <option value="DONE"></option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-link">SUBMIT</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>

        <div class="columns">
            <div class="column is-6">
                <h2 class="subtitle"> TO DO </h2>
                
                <div class="todo">
                    <div class="card">
                        <div class="card-content"> TASK DESCRIPTION </div>

                        <footer class="card-footer">
                            <a href="card-header-item">DONE</a>
                        </footer>
                    </div>
                </div>
            </div>
            <div class="column is-6">
                <h2 class="subtitle"> DONE </h2>
                
                <div class="todo">
                    <div class="card">
                        <div class="card-content"> TASK DESCRIPTION </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    name: 'Home',
    data() {
        return{

        }
    }
}
</script>