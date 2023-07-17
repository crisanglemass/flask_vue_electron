<template>
  <div>{{ msg }}</div>
</template>

<script>
export default {
  name: "GoProjectLogin",

  data() {
    return {
      msg: "",
    };
  },

  mounted() {
    this.auth();
  },

  methods: {
    auth() {
      const data = new FormData();
      this.$axios
        .post("/api/auth", data, {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        })
        .then((response) => {
          this.msg = response.data.data.msg;
        })
        .catch((error) => {});
    },
  },
};
</script>

<style lang="scss" scoped>
</style>