<template>
  <div class="card weather">
    <div class="d-flex justify-content-center row g-0">
      <div class="col-md-6 weatherDetails">
        <div class="d-flex flex-row">
          <div class="align-self-center">
            <i class="bi bi-cloud-drizzle weatherIcon"></i>
          </div>
          <div class="card-body weatherCard">
            <h5 class="card-title mb-0" style="font-weight: bold">
              <b>{{ weatherLocation }}</b>
            </h5>

            <p class="card-text">
              <span
                ><h3>
                  <strong>{{ weatherTemp }}</strong>
                  <span class="degree-celsius">&#8451;</span>
                </h3></span
              >
              <small class="text-muted"
                ><span class="weatherSync"
                  ><strong>{{ weatherTimeSync }}</strong></span
                ></small
              >
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      weatherLocation: "สายไหม",
      weatherDetails: "มีเมฆเล็กน้อย",
      weatherTimeSync: "เมื่อ 3 นาที ที่แล้ว",
      weatherTemp: "20.8",
    };
  },
};
</script>

<style lang="scss" scoped>
$card-bg: transparent;

.red {
  background-color: red;
}
.weather {
  margin: 25px;
  top: 0px;
  left: 3px;
}
.weatherIcon {
  color: white;
  font-size: 2rem;
}
.weatherDetails {
  color: white;
}
.weatherCard {
  padding: 10px 0px 0px 0px;
  color: white;
}
.weatherSync {
  color: white;
}
.degree-celsius {
  font-family: "Helvetica";
  font-weight: 600;
}
@import "/node_modules/bootstrap/scss/bootstrap.scss";
</style>
